# flake8: noqa

#!/usr/bin/env python3
import pathlib
import random

README = pathlib.Path("README.md")
START = "<!-- CHALLENGE:START -->"
END = "<!-- CHALLENGE:END -->"
CHALLENGE_LINK_START = "<!-- CHALLENGE_LINK:START -->"
CHALLENGE_LINK_END = "<!-- CHALLENGE_LINK:END -->"


def pick_kattis_problem():
    # Predefined list of beginner-friendly Kattis problems
    # Format: (problem_id, title, difficulty)
    beginner_problems = [
        ("hello", "Hello World!", "1.0"),
        ("carrots", "Carrots", "1.3"),
        ("potato", "Potato", "1.5"),
        ("2048", "2048", "1.7"),
        ("different", "A Different Problem", "1.8"),
        ("spavanac", "Spavanac", "2.0"),
        ("tri", "Triangle", "2.1"),
        ("rijeci", "Rijeci", "2.2"),
        ("kornislav", "Kornislav", "2.3"),
        ("pretpostavke", "Pretpostavke", "2.4"),
        ("abcd", "ABCD", "2.5"),
        ("karte", "Karte", "2.6"),
        ("trollhunt", "Troll Hunt", "2.7"),
        ("babylonian", "Babylonian Numbers", "2.8"),
        ("prva", "First", "2.9"),
        ("autori", "Autori", "3.0"),
        ("budilnik", "Budilnik", "3.1"),
        ("kockice", "Kockice", "3.2"),
        ("laptop", "Laptop", "3.3"),
        ("mali", "Mali", "3.4"),
    ]

    return random.choice(beginner_problems)


def pick_leetcode_problem():
    # Classic LeetCode problems everyone should attempt
    # Format: (problem_id, title, difficulty, category)
    classic_problems = [
        ("1", "Two Sum", "Easy", "Arrays"),
        ("2", "Add Two Numbers", "Medium", "Linked Lists"),
        ("3", "Longest Substring Without Repeating Characters", "Medium", "Strings"),
        ("5", "Longest Palindromic Substring", "Medium", "Strings"),
        ("7", "Reverse Integer", "Medium", "Math"),
        ("10", "Regular Expression Matching", "Hard", "Dynamic Programming"),
        ("11", "Container With Most Water", "Medium", "Arrays"),
        ("15", "3Sum", "Medium", "Arrays"),
        ("20", "Valid Parentheses", "Easy", "Stack"),
        ("21", "Merge Two Sorted Lists", "Easy", "Linked Lists"),
        ("22", "Generate Parentheses", "Medium", "Backtracking"),
        ("23", "Merge k Sorted Lists", "Hard", "Linked Lists"),
        ("26", "Remove Duplicates from Sorted Array", "Easy", "Arrays"),
        ("27", "Remove Element", "Easy", "Arrays"),
        ("28", "Find the Index of the First Occurrence in a String", "Easy", "Strings"),
        ("33", "Search in Rotated Sorted Array", "Medium", "Binary Search"),
        ("35", "Search Insert Position", "Easy", "Binary Search"),
        ("39", "Combination Sum", "Medium", "Backtracking"),
        ("42", "Trapping Rain Water", "Hard", "Arrays"),
        ("46", "Permutations", "Medium", "Backtracking"),
        ("48", "Rotate Image", "Medium", "Arrays"),
        ("49", "Group Anagrams", "Medium", "Hash Tables"),
        ("53", "Maximum Subarray", "Medium", "Dynamic Programming"),
        ("55", "Jump Game", "Medium", "Dynamic Programming"),
        ("56", "Merge Intervals", "Medium", "Arrays"),
        ("62", "Unique Paths", "Medium", "Dynamic Programming"),
        ("70", "Climbing Stairs", "Easy", "Dynamic Programming"),
        ("72", "Edit Distance", "Hard", "Dynamic Programming"),
        ("75", "Sort Colors", "Medium", "Arrays"),
        ("76", "Minimum Window Substring", "Hard", "Sliding Window"),
        ("78", "Subsets", "Medium", "Backtracking"),
        ("79", "Word Search", "Medium", "Backtracking"),
        ("84", "Largest Rectangle in Histogram", "Hard", "Stack"),
        ("88", "Merge Sorted Array", "Easy", "Arrays"),
        ("91", "Decode Ways", "Medium", "Dynamic Programming"),
        ("94", "Binary Tree Inorder Traversal", "Easy", "Trees"),
        ("98", "Validate Binary Search Tree", "Medium", "Trees"),
        ("101", "Symmetric Tree", "Easy", "Trees"),
        ("102", "Binary Tree Level Order Traversal", "Medium", "Trees"),
        ("104", "Maximum Depth of Binary Tree", "Easy", "Trees"),
        (
            "105",
            "Construct Binary Tree from Preorder and Inorder Traversal",
            "Medium",
            "Trees",
        ),
        ("114", "Flatten Binary Tree to Linked List", "Medium", "Trees"),
        ("121", "Best Time to Buy and Sell Stock", "Easy", "Arrays"),
        ("124", "Binary Tree Maximum Path Sum", "Hard", "Trees"),
        ("125", "Valid Palindrome", "Easy", "Strings"),
        ("128", "Longest Consecutive Sequence", "Medium", "Arrays"),
        ("136", "Single Number", "Easy", "Arrays"),
        ("139", "Word Break", "Medium", "Dynamic Programming"),
        ("141", "Linked List Cycle", "Easy", "Linked Lists"),
        ("146", "LRU Cache", "Medium", "Design"),
        ("148", "Sort List", "Medium", "Linked Lists"),
        ("152", "Maximum Product Subarray", "Medium", "Dynamic Programming"),
        ("155", "Min Stack", "Easy", "Stack"),
        ("160", "Intersection of Two Linked Lists", "Easy", "Linked Lists"),
        ("167", "Two Sum II - Input Array Is Sorted", "Medium", "Arrays"),
        ("169", "Majority Element", "Easy", "Arrays"),
        ("198", "House Robber", "Medium", "Dynamic Programming"),
        ("200", "Number of Islands", "Medium", "DFS/BFS"),
        ("206", "Reverse Linked List", "Easy", "Linked Lists"),
        ("215", "Kth Largest Element in an Array", "Medium", "Arrays"),
        ("217", "Contains Duplicate", "Easy", "Arrays"),
        ("226", "Invert Binary Tree", "Easy", "Trees"),
        ("234", "Palindrome Linked List", "Easy", "Linked Lists"),
        ("238", "Product of Array Except Self", "Medium", "Arrays"),
        ("283", "Move Zeroes", "Easy", "Arrays"),
        ("287", "Find the Duplicate Number", "Medium", "Arrays"),
        ("297", "Serialize and Deserialize Binary Tree", "Hard", "Trees"),
        ("300", "Longest Increasing Subsequence", "Medium", "Dynamic Programming"),
        ("322", "Coin Change", "Medium", "Dynamic Programming"),
        ("337", "House Robber III", "Medium", "Trees"),
        ("344", "Reverse String", "Easy", "Strings"),
        ("394", "Decode String", "Medium", "Stack"),
        ("416", "Partition Equal Subset Sum", "Medium", "Dynamic Programming"),
        ("424", "Longest Repeating Character Replacement", "Medium", "Sliding Window"),
        ("438", "Find All Anagrams in a String", "Medium", "Sliding Window"),
        ("461", "Hamming Distance", "Easy", "Bit Manipulation"),
        ("494", "Target Sum", "Medium", "Dynamic Programming"),
        ("538", "Convert BST to Greater Tree", "Medium", "Trees"),
        ("543", "Diameter of Binary Tree", "Easy", "Trees"),
        ("560", "Subarray Sum Equals K", "Medium", "Hash Tables"),
        ("581", "Shortest Unsorted Continuous Subarray", "Medium", "Arrays"),
        ("617", "Merge Two Binary Trees", "Easy", "Trees"),
        ("621", "Task Scheduler", "Medium", "Greedy"),
        ("647", "Palindromic Substrings", "Medium", "Strings"),
        ("674", "Longest Continuous Increasing Subsequence", "Easy", "Arrays"),
        ("704", "Binary Search", "Easy", "Binary Search"),
        ("739", "Daily Temperatures", "Medium", "Stack"),
        ("771", "Jewels and Stones", "Easy", "Hash Tables"),
        ("844", "Backspace String Compare", "Easy", "Stack"),
        ("876", "Middle of the Linked List", "Easy", "Linked Lists"),
        ("977", "Squares of a Sorted Array", "Easy", "Arrays"),
    ]

    return random.choice(classic_problems)


def update_readme():
    # Randomly choose between Kattis and LeetCode
    platform = random.choice(["kattis", "leetcode"])

    if platform == "kattis":
        pid, title, diff = pick_kattis_problem()
        mission = f'🤖 Mission uploaded: _Solve "{title}" [{diff} pts] on Kattis_'
        link = f"[Go solve it →](https://open.kattis.com/problems/{pid})"
        print(f"Updated with Kattis problem: {title}")
    else:
        pid, title, diff, category = pick_leetcode_problem()
        mission = (
            f'🤖 Mission uploaded: _Solve "{title}" [{diff}] - {category} on LeetCode_'
        )
        link = f"[Go solve it →](https://leetcode.com/problems/{title.replace(' ', '-').lower()}/)"
        print(f"Updated with LeetCode problem: {title}")

    text = README.read_text(encoding="utf-8")

    # Update the mission section first
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    temp_text = before + START + "\n" + mission + "\n" + END + after

    # Then update the challenge link section
    if CHALLENGE_LINK_START in temp_text and CHALLENGE_LINK_END in temp_text:
        link_before, link_rest = temp_text.split(CHALLENGE_LINK_START, 1)
        _, link_after = link_rest.split(CHALLENGE_LINK_END, 1)
        final_text = (
            link_before
            + CHALLENGE_LINK_START
            + "\n"
            + link
            + "\n"
            + CHALLENGE_LINK_END
            + link_after
        )
    else:
        final_text = temp_text

    README.write_text(final_text, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
