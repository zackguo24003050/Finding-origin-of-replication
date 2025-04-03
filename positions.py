def pattern_matching(pattern, genome):
    # Return all starting positions where 'pattern' appears in 'genome'
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)
    
    return positions


# Example
genome = "GATATATGCATATACTT"
pattern = "ATAT"
print(pattern_matching(pattern, genome))  
# Output: [1, 3, 9]
