#!/bin/bash
java -Xms256M -Xmx1024M -classpath ql.jar ca.uwaterloo.cs.ql.Main addcontain.ql c488_UnderstandFileDependency.contain c488_UnderstandFileDependency.raw.ta c488_UnderstandFileDependency.con.ta
cat schema.asv.ta c488_UnderstandFileDependency.con.ta > c488_UnderstandFileDependency.ls.ta
