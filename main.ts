// News-image entry program (Node 22, standard library only).
// The entry is the entry.png sitting next to this file. This program
// copies it into the output directory the grader provides, so the
// judge sees exactly the bytes of that file and nothing else.
//
// Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
