# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering algorithms, in contrast to k-means, naturally form clusters gradually by combining smaller clusters into larger ones. This gives them greater flexibility in responding to outliers."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Different runs of k-means can indeed produce different clusterings due to the random initialization of centroids, which may lead to different local optima. "

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is generally faster and less memory-intensive than agglomerative hierarchical clustering, it is not necessarily the most efficient algorithm possible."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "When a cluster is split during post-processing in k-means and points are reassigned to the closest centroid, the SSE is expected to decrease because points will be closer to their new centroid, thereby reducing the overall error"

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In k-means clustering, a decrease in SSE (improved cohesion) implies that points are closer to their respective centroids, which generally indicates better clustering."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSB indicates that clusters are farther apart from each other, which means that the separation between clusters has increased."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion and separation are independent in k-means clustering. Improving one does not necessarily mean the other will improve as well because they measure different aspects of the clustering quality."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + SSB is not a constant in k-means clustering. These two metrics depend on the positions of the centroids, which change during the clustering process."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = " In k-means, it's possible to improve cohesion without affecting or even while reducing separation, depending on the relative movement of centroids and the redistribution of data points."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The k-means method will probably place each centroid in the middle of each shaded circle by the conclusion of its execution given the uniform density of the shaded regions and the beginning centroids indicated by the X sign. This is because the centroids will move to the mean of the points inside their clusters."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Every shaded area in Figure (b) is distinct and contains an initial centroid. Assuming there is no overlap between the regions and the method performs as predicted with such discrete beginning placements, the k-means algorithm should converge with one centroid in the middle of each shaded region, with each cluster having just points from its respective region."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "In the case of Figure (c), it is improbable that the final clustering will contain an empty cluster given the initial centroids and the data points indicated by the red dots. Every data point in the k-means algorithm is paired with the closest centroid; because the centroids are positioned close to the points, each will probably draw in neighboring points, preventing any cluster from becoming empty after convergence."

    return answers



# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*(R^2)"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a)+(b*b)+(c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2)+((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Despite the difference in the number of points, the uniform distribution of points and the identical distances between the circles imply that there is no immediate need for the centroids to shift out of their initial circles."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 0

    # type: int
    answers["(b) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " Circle B's centroids are expected to move to Circle C due to its higher point density, leaving Circle B with no centroids. Circle A retains its single centroid, and Circle C ends up with three."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 1

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The single centroid from Circle A is likely to be shared with Circle B due to their closeness, leaving Circle A with no centroids, Circle B with one, and Circle C with its two initial centroids due to its large number of points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A" , "Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B would be considered for merging because the single link technique merges clusters based on the closest pair of points, and these two groups have the closest pair of points among all."

    # type: set
    answers["(b)"] = {"Group A" , "Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " Groups A and C would be considered for merging because the complete link technique considers the farthest pair of points for merging, and the farthest points of Groups A and C are closer than those of Groups A and B."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B','C','E','F','G'}

    # type: set
    answers["(a) boundary"] = {'D'}

    # type: set
    answers["(a) noise"] = {'A','H','M'}

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers





# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 3"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The cluster with the largest clustering entropy would be the one that has the most uniform distribution of categories, as this would indicate the most disorder. From the provided table, Cluster 3 seems to have the most uniform distribution across different land covers, and therefore, would have the largest clustering entropy."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " The cluster with the smallest clustering entropy would be the one with the least uniform distribution of categories, meaning most of the data points in the cluster belong to one category. Cluster 1 is predominantly water with 9000 out of 10000 points being water, indicating a very well-defined grouping and thus the smallest clustering entropy."

    return answers



# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = "Dataset X"
    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = "Cluster D"

    # type: string
    answers["(b) Row 2"] = "Cluster A"

    # type: string
    answers["(b) Row 3"] = "Cluster B"

    # type: string
    answers["(b) Row 4"] = "Cluster C"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "Overlapping"," Partial" ]

    # type: list
    answers["(b)"] = ["Partitional", "Exclusive", "Complete"]
    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Students are assigned to distinct job categories without overlap (e.g., TA, RA, other on-campus jobs, jobless), fitting partitional and exclusive clustering. The requirement that assignments sum to 20 hours necessitates a complete categorization of all students."

    # type: list
    answers["(c)"] = ["Partitional", "Exclusive", "Complete"]
    
    # type: list
    answers["(d)"] = ['Hierarchical", "Overlapping", "Partial ']
    
    # type: list
    answers["(e)"] = ["Partitional", "Exclusive","Complete"]
    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Grading inherently divides students into distinct, non-overlapping categories (e.g., letter grades), fitting partitional and exclusive clustering. All students receive a grade, necessitating a complete clustering approach."

   

    return answers


# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "For figure (a), DBSCAN could potentially identify the patterns of the nose, eyes, and mouth if the points representing these features are in relatively denser regions compared to the rest of the face. DBSCAN works by identifying 'core points' in dense regions and expanding clusters from them.For figure (b), which seems to have a more uniform distribution of points, DBSCAN might struggle if the density in the regions of the features (nose, eyes, mouth) is not sufficiently higher than the surrounding areas."

    # type: string
    answers["(b) Figure (a)"] = "Yes"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For both figures, K-Means could be used to find patterns if we specify the number of clusters corresponding to the number of features we want to identify (for example, two for the eyes, one for the nose, and one for the mouth). However, K-Means assumes that clusters are spherical and evenly sized, which might not be the case here, especially if the distribution of points for each feature is not circular or if they vary significantly in size."

    # type: string
    answers["(c)"] = "k-means"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
