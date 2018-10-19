#!/bin/bash
echo $#;
if [ $# -le 4 ]; then
    echo "USAGE: ${0} productionDirName inputDirName nevents seedingThredhold gatheringThrehold";
    exit 1;
fi

PRODDIR=$1
INDIR=$2
NEVTS=$3
SEED=$4
GATHER=$5

############ BATCH QUEUE DIRECTIVES ##############################
# FOR SOME REASON IT DOESN T LIKE DIRECTIVES FROM COMMAND LINE!!!!!!!!!!
# Job name (defines name seen in monitoring by qstat and the
#     job script's stderr/stdout names)
#$ -N generation_example

### Specify the queue on which to run
#$ -q all.q

# Change to the current working directory from which the job got
# submitted (will also result in the job report stdout/stderr being
# written to this directory)
#$ -cwd

# here you could change location of the job report stdout/stderr files
#  if you did not want them in the submission directory
# #$ -o some_dir
# #$ -e some_dir

##################################################################

##### CONFIGURATION ##############################################
#ENVDIR=/shome/mratti/cmssw_workarea/Generation/CMSSW_10_0_3_mod/src # use the startsdir instead to set the environment
DBG=1
### do not change below
SEOUTFILES="EGM-RunIISpring18_GEN_SIM_DIGI_RECO.root"
SHORTJOBDIR="NEVTS"$NEVTS"_seed"$SEED"_GATHER"$GATHER
JOBDIR=$SHORTJOBDIR"_"$JOB_ID
STARTDIR=`pwd`
TOPWORKDIR=/scratch/`whoami` # Top working directory on worker node's local disk, where the batch working dir is
SE_PREFIX="root://t3dcachedb.psi.ch:1094/"
USER_SE_AREA="/pnfs/psi.ch/cms/trivcat/store/user"
SERESULTDIR=$USER_SE_AREA/mratti/$PRODDIR/$SHORTJOBDIR
SEINDIR=$USER_SE_AREA/mratti/$INDIR
##################################################################

##### SET UP WORKDIR ######################################################
WORKDIR=$TOPWORKDIR/$JOBDIR
if test -e "$WORKDIR"; then
   echo "ERROR: WORKDIR ($WORKDIR) already exists! Aborting..." >&2
   #exit 1
fi
mkdir -p $WORKDIR
if test ! -d "$WORKDIR"; then
   echo "ERROR: Failed to create workdir ($WORKDIR)! Aborting..." >&2
   #exit 1
fi

cd $WORKDIR
###########################################################################

##### MONITORING INFORMATION #####################################
DATE_START=`date +%s`
echo "Job started at " `date`
cd $WORKDIR
cat <<EOF
## QUEUEING SYSTEM SETTINGS:
HOME=$HOME
USER=$USER
JOB_ID=$JOB_ID
JOB_NAME=$JOB_NAME
HOSTNAME=$HOSTNAME
TASK_ID=$TASK_ID
QUEUE=$QUEUE

## JOB SETTINGS:
##ENVDIR=$ENVDIR
STARTDIR=$STARTDIR
WORKDIR=$WORKDIR
SERESULTDIR=$SERESULTDIR
EOF
###########################################################################

###########################################################################
## YOUR FUNCTIONALITY CODE GOES HERE

source $VO_CMS_SW_DIR/cmsset_default.sh
shopt -s expand_aliases

#cd $ENVDIR
cd $STARTDIR
cmsenv

cd $WORKDIR
cp $STARTDIR/step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py .
xrdcp $SE_PREFIX/$SEINDIR/EGM-RunIISpring18_GEN_SIM_DIGI.root .
echo 'Going to run step 3'
cmsRun step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py maxEvents=$NEVTS EBseed=$SEED EEseed=$SEED EBgather=$GATHER EEgather=$GATHER

###########################################################################


#### RETRIEVAL OF OUTPUT FILES AND CLEANING UP ############################
cd $WORKDIR
echo "########################################################"
echo "############# Working directory contents ###############"
echo "pwd: " `pwd`
ls -Rl
echo "########################################################"
echo "YOUR OUTPUT WILL BE MOVED TO $SERESULTDIR"
echo "########################################################"

xrdfs t3dcachedb03.psi.ch mkdir $SERESULTDIR

if test x"$SEOUTFILES" != x; then
   if test 0"$DBG" -ge 2; then
      xrdcpdebug="-d 2"
   fi
   for n in $SEOUTFILES; do
       if test ! -e $WORKDIR/$n; then
          echo "WARNING: Cannot find output file $WORKDIR/$n. Ignoring it" >&2
       else
          xrdcp $xrdcpdebug $WORKDIR/$n $SE_PREFIX/$SERESULTDIR/$n
          if test $? -ne 0; then
             echo "ERROR: Failed to copy $WORKDIR/$n to $SERESULTDIR/$n" >&2
          fi
   fi
   done
fi


echo "Cleaning up $WORKDIR"
rm -rf $WORKDIR

###########################################################################
DATE_END=`date +%s`
RUNTIME=$((DATE_END-DATE_START))
echo "################################################################"
echo "Job finished at " `date`
echo "Wallclock running time: $RUNTIME s"
#exit 0
