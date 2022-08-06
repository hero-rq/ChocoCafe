def create_dataframe_survived_rate(feature):
	survived = train[train['Survived']==1][feature].value_counts()

	dead = train[train['Survived']==0][feature].value_counts()
	df_graph = pd.DataFrame([survived, dead])
	df_graph.index = ['Survived', 'Dead']

	retyrn df_graph 
