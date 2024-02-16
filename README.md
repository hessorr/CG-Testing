## Chain Graph Testing with using R packages
### This repo is used to test the pc gaussian accuracy in the lcdv2 R package

- cg_2_50 contains 60 csv files. All files have a degree of 2 with 50 nodes. 30 of these files are the original CG generated with create_random_mat.R. 30 of these (labeled with _pattern) are the pattern of the 30 orginal CGs. Patterns generated with pattern() fucntion from lcdv2
- cg_2_50 contains 60 csv files. All files have a degree of 3 with 50 nodes. 30 of these files are the original CG generated with create_random_mat.R. 30 of these (labeled with _pattern) are the pattern of the 30 orginal CGs. Patterns generated with pattern() fucntion from lcdv2
- create_random_mat.R is Dr.Javidian's code for generating adjacency matricies that are CGs
- generate_pattern_of_cgs.R is code to generate the pattern of the CGS
