def frequent_words(text, k):
    """
    Return the most frequent k-mers in the given text.
    """
    words = []
    freq_map = frequency_map(text, k)
    max_count = max(freq_map.values())

    for kmer in freq_map:
        if freq_map[kmer] == max_count:
            words.append(kmer)

    return words


def frequency_map(text, k):
    """
    Return a frequency map of all k-mers of length k in text.
    """
    freq = {}
    n = len(text)

    for i in range(n - k + 1):
        kmer = text[i:i + k]
        freq[kmer] = freq.get(kmer, 0) + 1  # cleaner way to count

    return freq


# Example
dna = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
print(frequent_words(dna, 2))

def reverse_complement(pattern):
    # Return the reverse complement of a DNA string
    return complement(reverse(pattern))

def reverse(pattern):
    # Return the reversed string
    return pattern[::-1]

def complement(pattern):
    # Return the complement (A↔T, C↔G)
    comp = ''
    for base in pattern:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A"
        elif base == "C":
            comp += "G"
        elif base == "G":
            comp += "C"
    return comp

# Example
print(reverse_complement("ATCGTA"))  # Output: TACGAT
