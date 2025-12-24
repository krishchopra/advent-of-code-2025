#!/usr/bin/env bun

const inputPath = `${import.meta.dir}/data.txt`;
const input = await Bun.file(inputPath).text();
const lines = input.trim().split("\n");
const CHECK_LIMIT = 1000;

const distance = (
  point1: [number, number, number],
  point2: [number, number, number]
): number => {
  const [x1, y1, z1] = point1;
  const [x2, y2, z2] = point2;
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5;
};

const hash = (
  point1: [number, number, number],
  point2?: [number, number, number]
): string => {
  if (point2) {
    return `${point1[0]},${point1[1]},${point1[2]}|${point2[0]},${point2[1]},${point2[2]}`;
  }
  return `${point1[0]},${point1[1]},${point1[2]}`;
};

// given point, finds its root parent (parent of itself is itself)
const find = (point: string, parents: Map<string, string>) => {
  const parent = parents.get(point);
  if (parent == point) return point;
  if (parent) return find(parent, parents);
};

// given two points, set smaller rank's parent equal to larger rank parent
// if same rank, arbitrarily choose one and increase rank by one
const union = (
  p1: string,
  p2: string,
  parents: Map<string, string>,
  ranks: Map<string, number>
) => {
  const [p1Parent, p2Parent] = [find(p1, parents), find(p2, parents)];
  if (!p1Parent || !p2Parent) {
    console.log(`parent not found for ${p1}, ${p2}`);
    return;
  }
  const [p1Rank, p2Rank] = [ranks.get(p1Parent), ranks.get(p2Parent)];
  if (p1Rank === undefined || p2Rank === undefined) {
    console.log(`rank not found for ${p1Parent}, ${p2Parent}`);
    return;
  }
  if (p1Rank > p2Rank) {
    parents.set(p2Parent, p1Parent);
  } else if (p2Rank > p1Rank) {
    parents.set(p1Parent, p2Parent);
  } else {
    parents.set(p2Parent, p1Parent);
    ranks.set(p1Parent, p1Rank + 1);
  }
};

// construct array of points
const points = new Array<[number, number, number]>();
for (const line of lines) {
  const [x, y, z] = line.split(",");
  points.push([parseInt(x), parseInt(y), parseInt(z)]);
}

const distances = new Map<string, number>();
const parents = new Map<string, string>(); // map of point to its parent point
const ranks = new Map<string, number>(); // ranks map, from parent tree to its max height
const sizes = new Map<string, number>();

// union find + dsu
for (let i = 0; i < points.length; i++) {
  // initialize the parents and ranks map
  parents.set(hash(points[i]), hash(points[i]));
  ranks.set(hash(points[i]), 0);
  sizes.set(hash(points[i]), 0);
  for (let j = i + 1; j < points.length; j++) {
    const dist = distance(points[i], points[j]);
    distances.set(hash(points[i], points[j]), dist);
  }
}

const sortedDistances = new Map(
  [...distances.entries()].sort((a, b) => a[1] - b[1])
);

const sortedDistancePairs = sortedDistances.keys().toArray();

for (let i = 0; i < CHECK_LIMIT; i++) {
  const [p1, p2] = sortedDistancePairs[i].split("|");
  union(p1, p2, parents, ranks);
}

for (let i = 0; i < points.length; i++) {
  const p = find(hash(points[i]), parents);
  if (p) {
    const currentSize = sizes.get(p) || 0;
    sizes.set(p, currentSize + 1);
  }
}

const sortedSizes = [...sizes.entries()].sort((a, b) => b[1] - a[1]);
console.log(sortedSizes.slice(0, 3));

export {};
