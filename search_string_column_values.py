#This code is extracted from: https://labs.cognitiveclass.ai/tools/jupyterlab/DS0103EN-3-3-1-From-Understanding-to-Preparation-v2.0
ingredients = list(recipes.columns.values)

print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(rice).*")).search(ingredient)] if match])
