#!/bin/bash
#YBATCH -r dgx-a100_1
#SBATCH -N 1
#SBATCH --output outputs/%j.out

source /etc/profile.d/modules.sh
module load cuda/12.1 nccl/cuda-11.7/2.14.3 clang/15.0

CUDA_VISIBLE_DEVICES=0 python pred.py --model ${1}

