######### qsub -o ./ -e ./ -N digi -q long.q -pe smp 8  -cwd ecalDigi_template.sh


# Job configuration
JOBOPFILENAME="step2_DoublePhoton.py"
FILENAME="EGM_GEN_SIM_DIGI.root"
INFILENAME="EGM_GEN_SIM.root"
SERESULTDIR="/pnfs/psi.ch/cms/trivcat/store/user/mratti/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/105X_upgrade2018_realistic_v3/"

STARTDIR=`pwd`
TOPWORKDIR="/scratch/mratti/"
JOBDIR="gen_"$JOB_ID
WORKDIR=$TOPWORKDIR/$JOBDIR
SEPREFIX="root://t3dcachedb.psi.ch:1094/"




# Job instructions
source $VO_CMS_SW_DIR/cmsset_default.sh
shopt -s expand_aliases

echo ""
echo "Going to set up cms environment"
cd $STARTDIR
cmsenv

echo ""
echo "Going to create work dir"
mkdir -p $WORKDIR

echo ""
echo "Going to copy cms driver"
cp $JOBOPFILENAME $WORKDIR/$JOBOPFILENAME

echo ""
echo "Going to copy input file"
xrdcp  $SEPREFIX/$SERESULTDIR/$INFILENAME $WORKDIR/$INFILENAME

cd $WORKDIR

echo ""
echo "Going to run"

DATE_START=`date +%s`
cmsRun $JOBOPFILENAME 
DATE_END=`date +%s`

echo ""
echo "Finished running"

echo ""
echo "Content of current directory"
ls -al

echo ""
echo "Going to copy output to storage element area"
xrdcp $FILENAME $SEPREFIX/$SERESULTDIR/$FILENAME

echo ""
echo "Cleaning up $WORKDIR"
rm -rf $WORKDIR

RUNTIME=$((DATE_END-DATE_START))
echo "Wallclock running time: $RUNTIME s"




