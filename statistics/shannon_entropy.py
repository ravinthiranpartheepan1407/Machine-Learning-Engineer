# Entropy was used mostly in Information Tranportation : FTP,...

# Shannon Entropy: USed to measure how many information is required to describe something based on how many different possibilities.

# For example, If you are playing a guessing game with your friend and your friend though number 47 in his mind and you guessed 43.
# You ask for hint and your friend gives a hint that you guess should be little bit higher from guessed value.

# Shannon Entropy uses: Probability (p) and Data Values (x[index])

### Formula: -(sum (p(x[index]) log2(p(x[index])) )) # If log2 value si bettewn 0 to 1 it will gives only -ve values

# Suitable data: only Nominal, Ordinal and Discrete
# If we have Interval or Ratio data: Should be converted to discrete by histogram creation

### Important: Entropy depends on bin size and number.

# High Enrtopy (If the area between the curves has wide fatness): Dataset has lot of dispersion / variablility.
# Low entropy (If the curves has lesser fatness): Data has lot of repeated values.

# How entropy differs from variance:

 # - Entropy: Non linear and make no assumptions about the dataset\
 # - Variance: Depends on the validity of the mean and appropriate for roughly normal data

# Bits: use log2 - Measure between 0 to 1:                          -(sum (p(x[index]) log2(p(x[index])) ))
# Nats: use ln (Natural Log) - Measure between different datasets:  -(sum (p(x[index]) ln(p(x[index])) ))

