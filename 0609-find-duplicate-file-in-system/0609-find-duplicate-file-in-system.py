class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        keys = {}

        for path in paths:
            parts = path.split(" ")
            root = parts[0]

            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]
                full_path = root + "/" + name

                if content not in keys:
                    keys[content] = [full_path]
                else:
                    keys[content].append(full_path)

        result = []
        for content in keys:
            if len(keys[content]) > 1:
                result.append(keys[content])

        return result
