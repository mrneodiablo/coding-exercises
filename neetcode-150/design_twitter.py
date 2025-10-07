"""
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId)
Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId)
Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted
by users who the user followed or by the user themself.
Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId)
The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId)
The user with ID followerId started unfollowing the user with ID followeeId.
"""

from typing import List
import heapq
import unittest


class Twitter:

    def __init__(self):
        self.data = {}
        self.timestamp = 0  # Global timestamp for tweet ordering

    def initUser(self, userId: int) -> None:
        if userId not in self.data:
            self.data[userId] = {"posts": [], "followees": set()}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.initUser(userId)
        # Store tweet with timestamp for proper ordering
        # (most recent = higher timestamp)
        self.data[userId]["posts"].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.initUser(userId)

        # Use max-heap (simulate with negative timestamps)
        # to get top 10 most recent tweets
        # Heap stores: (-timestamp, tweetId) -
        # min-heap with negative values = max-heap
        max_heap = []

        # Helper function to add only top 10 recent tweets to heap
        def add_recent_tweets_to_heap(tweets):
            # Only take the 10 most recent tweets from this user
            recent_tweets = tweets[-10:] if len(tweets) > 10 else tweets
            for timestamp, tweetId in recent_tweets:
                heapq.heappush(max_heap, (-timestamp, tweetId))

        # Add user's own top 10 recent tweets
        add_recent_tweets_to_heap(self.data[userId]["posts"])

        # Add top 10 recent tweets from each followee
        for followeeId in self.data[userId]["followees"]:
            if followeeId in self.data:
                add_recent_tweets_to_heap(self.data[followeeId]["posts"])

        # Extract top 10 most recent tweets (largest timestamps first)
        result = []
        for _ in range(min(10, len(max_heap))):
            _, tweetId = heapq.heappop(max_heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.initUser(followerId)
        self.initUser(followeeId)  # Initialize followee too

        # Don't allow following yourself
        if followerId != followeeId:
            self.data[followerId]["followees"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.initUser(followerId)

        # Safe removal - only remove if exists
        if followeeId in self.data[followerId]["followees"]:
            self.data[followerId]["followees"].remove(followeeId)

        # Safe removal - only remove if exists
        if followeeId in self.data[followerId]["followees"]:
            self.data[followerId]["followees"].remove(followeeId)


class TestTwitter(unittest.TestCase):
    def setUp(self):
        self.twitter = Twitter()

    def test_case_1_basic_functionality(self):
        """Test case 1: Basic post and news feed functionality"""
        # User 1 posts tweets
        self.twitter.postTweet(1, 5)
        self.twitter.postTweet(1, 3)

        # User 1's news feed should show their own tweets (most recent first)
        news_feed = self.twitter.getNewsFeed(1)
        expected = [3, 5]  # Most recent first
        self.assertEqual(news_feed, expected)

    def test_case_2_follow_and_unfollow(self):
        """Test case 2: Follow/unfollow functionality with news feed"""
        # User 1 follows user 2
        self.twitter.follow(1, 2)

        # User 2 posts a tweet
        self.twitter.postTweet(2, 6)

        # User 1's news feed should include user 2's tweet
        news_feed = self.twitter.getNewsFeed(1)
        expected = [6]
        self.assertEqual(news_feed, expected)

        # User 1 unfollows user 2
        self.twitter.unfollow(1, 2)

        # User 1's news feed should be empty now
        news_feed = self.twitter.getNewsFeed(1)
        expected = []
        self.assertEqual(news_feed, expected)

    def test_case_3_complex_scenario(self):
        """Test case 3: Complex scenario with multiple users and tweets"""
        # User 1 posts tweets
        self.twitter.postTweet(1, 1)
        self.twitter.postTweet(1, 2)

        # User 1 follows user 2
        self.twitter.follow(1, 2)

        # User 2 posts tweets
        self.twitter.postTweet(2, 3)
        self.twitter.postTweet(2, 4)

        # User 1's news feed should show all tweets in chronological order
        news_feed = self.twitter.getNewsFeed(1)
        expected = [4, 3, 2, 1]  # Most recent first
        self.assertEqual(news_feed, expected)

        # User 1 follows user 3
        self.twitter.follow(1, 3)

        # User 3 posts tweets
        self.twitter.postTweet(3, 5)
        self.twitter.postTweet(3, 6)

        # User 1's news feed should include user 3's tweets
        news_feed = self.twitter.getNewsFeed(1)
        expected = [6, 5, 4, 3, 2, 1]  # Most recent first
        self.assertEqual(news_feed, expected)


def manual_test():
    """Manual testing with detailed output"""
    print("=" * 50)
    print("DESIGN TWITTER - TEST CASES")
    print("=" * 50)

    twitter = Twitter()

    print("Test 1: Basic functionality")
    twitter.postTweet(1, 5)
    print("  User 1 posts tweet 5")

    news_feed = twitter.getNewsFeed(1)
    print(f"  User 1's news feed: {news_feed}")
    print(f"  Expected: [5] - ✅ {'PASSED' if news_feed == [5] else 'FAILED'}")
    print()

    print("Test 2: Follow functionality")
    twitter.follow(1, 2)
    print("  User 1 follows user 2")

    twitter.postTweet(2, 6)
    print("  User 2 posts tweet 6")

    news_feed = twitter.getNewsFeed(1)
    print(f"  User 1's news feed: {news_feed}")
    expected = [6, 5]  # Most recent first
    print(
        f"  Expected: {expected} - ✅ {'PASSED' if
                                      news_feed == expected
                                      else 'FAILED'}"
    )
    print()

    print("Test 3: Unfollow functionality")
    twitter.unfollow(1, 2)
    print("  User 1 unfollows user 2")

    news_feed = twitter.getNewsFeed(1)
    print(f"  User 1's news feed: {news_feed}")
    expected = [5]  # Only own tweets
    print(
        f" Expected: {expected} - ✅ {'PASSED' if
                                     news_feed == expected
                                     else 'FAILED'}"
    )


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()
