def chou_fasman(sequence):
  """Predicts alpha-helices and beta-sheets using the Chou-Fasman method.

  Args:
    sequence: The protein sequence as a string.

  Returns:
    A list of predicted secondary structures (H for helix, E for sheet, C for coil).
  """

  # Simplified amino acid propensities (replace with actual values)
  helix_propensity = {'A': 1.42, 'L': 1.34, 'S': 0.74, 'E': 1.25, 'G': 0.54}
  sheet_propensity = {'V': 1.14, 'I': 1.05, 'Y': 0.74, 'F': 1.19, 'C': 0.71}

  # Other amino acids have propensities, but we'll simplify for this example

  prediction = []
  for i in range(len(sequence)):
    helix_sum = 0
    sheet_sum = 0
    for j in range(i, min(i+6, len(sequence))):
      aa = sequence[j]
      helix_sum += helix_propensity.get(aa, 0)
      sheet_sum += sheet_propensity.get(aa, 0)
    if helix_sum >= 100:
      prediction.append('H')
    elif sheet_sum >= 100:
      prediction.append('E')
    else:
      prediction.append('C')

  return prediction