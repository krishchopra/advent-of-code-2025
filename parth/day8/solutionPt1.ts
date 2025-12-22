#!/usr/bin/env bun

const inputPath = `${import.meta.dir}/data.txt`;
const input = await Bun.file(inputPath).text();
const lines = input.trim().split("\n");

lines.slice(0, 5).forEach((line, index) => {
  console.log(`${index + 1}: ${line}`);
});

export {};
