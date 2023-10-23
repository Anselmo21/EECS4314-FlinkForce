confile = $1;	// CONTAIN
rawfile = $2;	// .raw.ta
outfile = $3;

contain = eset;
getdb(confile);

///// Verify input contain.
ideg = indegree(contain);
ents = dom ideg - ideg . {1};
if(#ents > 0) {
    print "  Error[addcon.ql]: illegal contain";
    form(contain o ents, "    ", "&0", "&1");
    exit;
}
delete ideg;
delete ents;

confiles = rng contain - dom contain;

///// Read raw data
contain = eset;
getta(rawfile);

toSave = relnames;

files = $INSTANCE . {"cFile","cFunction"};
files1 = files ^ (dom contain - rng contain);
files2 = files - ent contain;
files = files1 + files2;

extra = confiles - files;
if(#extra > 0) {
    print "  Error[addcontain.ql]: extra files included in contain";
    form(sort(extra), "    ", "&0");
    exit;
}

ignore = files - confiles;
if(#ignore > 0) {
    print "  Warning[addcontain.ql]: files not included in contain are ignored";
    form(sort(ignore), "    ", "&0");

    Do = contain*;
    delset(ignore . Do);
    delete Do;
}

///////////////////////////////////////////////////////////////////////
///// Read contain file again to avoid the unexpected effect by delset.
getdb(confile);
$INSTANCE = $INSTANCE + (ent contain - dom $INSTANCE) X {"cSubSystem"};

putta(outfile, toSave);

