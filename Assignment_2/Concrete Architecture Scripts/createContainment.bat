java -Xms256M -Xmx1024M -classpath ql.jar ca.uwaterloo.cs.ql.Main addcontain.ql flink_UnderstandFileDependency.contain flink_UnderstandFileDependency.raw.ta flink_UnderstandFileDependency.con.ta
type schema.asv.ta flink_UnderstandFileDependency.con.ta > flink_UnderstandFileDependency.ls.ta
pause