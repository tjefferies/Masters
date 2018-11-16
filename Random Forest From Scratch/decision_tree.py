from util import entropy, information_gain, partition_classes
import numpy as np 
import ast

class DecisionTree(object):

    """
    DecisionTree splits on each column in X
    based on max information_gain.

    The tree continues to split until it hits `self.max_depth`
    or
    all nodes have a single label.

    """

    def __init__(self):
        # Initializing the tree as an empty dictionary or list, as preferred
        #self.tree = []
        self.tree = {}
        self.max_depth = 50

    def find_most_frequently_occuring_y_value(self, y):
        """
        Returns the most frequently occurring label
        from set of y labels

        Args:
            y: array of labels

        Returns:
            The most frequently occurring label

        """
        value, count = np.unique(y, return_counts=True)
        max_index = np.argmax(count)
        return value[max_index]

    def bool_if_only_one_unique_y_left(self, y):
        """
        Returns True if there's only one unique y left
        Else
        False

        If there is only one unique y value left,
        the decision tree has partitioned the data set
        to the lowest level of granularity where the leaf
        contains a single value

        Args:
            y: array of labels

        Returns:
            bool

        """
        value, count = np.unique(y, return_counts=True)
        if len(value) == 1:
            return True
        else:
            return False

    def split_tree_based_on_max_info_gain(self, X, y):
        """
        Returns True if there's only one unique y left
        Else
        False

        If there is only one unique y value left,
        the decision tree has partitioned the data set
        to the lowest level of granularity where the leaf
        contains a single value

        Args:
            y: array of labels

        Returns:
            bool

        """
        split_value = X[0][0]
        row_one = X[0]
        split_column, max_info_gain = 0, 0

        for column in range(len(row_one)):
            unique_column = set([row[column] for row in X])
            for value in unique_column:
                y_left, y_right = partition_classes(X, y, column, value)[2:4]
                info_gain = information_gain(y, [y_left, y_right])
                if info_gain > max_info_gain:
                    max_info_gain = info_gain
                    split_column, split_value = column, value
        return split_column, split_value


    def grow_decision_tree(self, X, y, depth):
        """
        Recursive function that calls itself until
        the max depth is reached or there is only
        label remaining. At this point, either
        return the lone remaining label
        or
        return the most frequently occurring label

        1) First split data based on maximum information gain
        2) Next partition the features and labels
        3.1) If no features are returned from the partition,
            return the most frequently occurring label
        3.2) Else grow the tree based on the split_column and
            the split_value determined by maximum information gain

        Args:
            X: array of features
            y: array of labels
            depth: number of splits to perform

        Returns:
            decision_tree: dict representation of the decision tree

        """
        if depth >= self.max_depth:
            return self.find_most_frequently_occuring_y_value(y)
        if self.bool_if_only_one_unique_y_left(y):
            return y[0]
        split_column, split_value = self.split_tree_based_on_max_info_gain(X, y)
        X_left, X_right, y_left, y_right = partition_classes(X, y, split_column, split_value)
        if len(X_left) == 0 or len(X_right) == 0:
            return self.find_most_frequently_occuring_y_value(y)
        else:
            decision_tree = dict()
            decision_tree[split_column] = [split_value, self.grow_decision_tree(X_left, y_left, depth + 1),
                                 self.grow_decision_tree(X_right, y_right, depth + 1)]
            return decision_tree

    def learn(self, X, y):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        '''
        build the tree by splitting X until all nodes have a single label.
        '''
        if len(y) == 0:
            self.tree['valid'] = None

        self.tree = self.grow_decision_tree(X, y, 1)


    def classify(self, record):
        # TODO: classify the record using self.tree and return the predicted label
        trained_decision_tree = self.tree
        while isinstance(trained_decision_tree, dict):
            split_column = list(trained_decision_tree.keys())[0]
            split_value = trained_decision_tree[split_column][0]
            if isinstance(split_value, str):
                if record[split_column] == split_value:
                    trained_decision_tree = trained_decision_tree[split_column][1]
                else:
                    trained_decision_tree = trained_decision_tree[split_column][2]
            else:
                if record[split_column] <= split_value:
                    trained_decision_tree = trained_decision_tree[split_column][1]
                else:
                    trained_decision_tree = trained_decision_tree[split_column][2]
        return trained_decision_tree 