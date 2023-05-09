# In histogram bins size does matter a lot for measuring dispersion

# How to calculate bin: k = ceil(max(x) - min(x)) / h
# Where k = no.of bins and h = width of a bin
# Ceil rounds-up to the next value (For ex: if the value os 2.01 then it will be 3.0)

# How many bins?
    # Struges (Depends on data count: If the data is larger then the bins will also be larger): k = ceil(log2(x)) + 1  # Note: Log always increase
    # Freedman-Diaconis[Common Choice] (Depends on Data count and data spread): h = 2 * IQR/cube_root(n) where IQR = Q1-Q3
        # If IQR gets larger: Larger dispersion || total bin size will also larger || no.of bins will decrease
        # If n gets larger: Bin width gets smaller || that results larger no.of bins
    # Arbitrary: (Intution Based) k = some_value