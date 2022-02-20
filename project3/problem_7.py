# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_segment):
        # Insert the node as before
        self.children[path_segment] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # start at root
        current_node = self.root

        for segment in path:
            # insert it if it doesn't exist already
            if segment not in current_node.children.keys():
                current_node.insert(segment)

            # update the current node
            current_node = current_node.children[segment]

        # add handler to leaf
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # start at root
        current_node = self.root

        # if path only has empty string, then this is root
        if (path != [""]):
            for segment in path:
                # return None if it doesn't exist
                if segment not in current_node.children.keys():
                    return None

                # update the current node
                current_node = current_node.children[segment]

        # return handler or None
        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.trie.find(self.split_path(path))
        if handler == None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        # split the path into path segments
        # knock off a trailing "/" - for bonus points :-)
        if path[-1] == "/":
            path = path[0:-1]
        if len(path) > 0 and path[0] == "/":
            path_list = path[1:].split("/")
            return path_list
        return path.split("/")


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

# some more testing for fun :-)
# create a different router and add a route
another_router = Router(
    "root handler", "404 - \"It's a trap!\", exclaimed Admiral Ackbar, to no one in particular.")
another_router.add_handler(
    "/products/shamwows", "shamwows handler")  # add a route
another_router.add_handler("/products/shamwows/blue",
                           "blue shamwow handler")  # add a route

# some lookups with the expected output
print(another_router.lookup("/"))  # should print 'root handler'
# should print '404 - "It's a trap!", exclaimed Admiral Ackbar, to no one in particular.'
print(another_router.lookup("/home"))
# should print '404 - "It's a trap!", exclaimed Admiral Ackbar, to no one in particular.'
print(another_router.lookup("/products"))
# should print 'shamwows handler'
print(another_router.lookup("/products/shamwows"))
# should print 'blue shamwow handler'
print(another_router.lookup("/products/shamwows/blue"))
# should print '404 - "It's a trap!", exclaimed Admiral Ackbar, to no one in particular.'
print(another_router.lookup("/products/shamwows/red"))
