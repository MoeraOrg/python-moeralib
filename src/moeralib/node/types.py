# This file is generated

from typing import List, Literal, Mapping, TypeAlias

from ..structure import Structure

Timestamp: TypeAlias = int
PrincipalValue: TypeAlias = str

AskSubject = Literal["subscribe", "friend"]

BlockedEntryOperation = Literal["addComment", "addReaction"]

BlockedOperation = Literal["reaction", "comment", "posting", "visibility", "instant"]

BodyFormat = Literal["message", "application"]

DraftType = Literal["new-posting", "posting-update", "new-comment", "comment-update"]

OperationStatus = Literal["waiting", "added", "started", "succeeded", "failed", "unknown"]

PrincipalFlag = Literal[
    "none", "private", "admin", "owner", "secret", "senior", "enigma", "major", "signed", "subscribed", "public",
    "friends", "unset"
]

PushContentType = Literal["story-added", "story-deleted", "feed-updated"]

PushRelayType = Literal["fcm"]

SettingType = Literal[
    "bool", "int", "string", "json", "Duration", "PrivateKey", "PublicKey", "Timestamp", "UUID", "Principal"
]

SheriffComplaintStatus = Literal[
    "posted", "prepared", "prepare-failed", "not-found", "invalid-target", "not-original", "not-sheriff", "approved",
    "rejected"
]

SheriffOrderCategory = Literal["visibility"]

SheriffOrderReason = Literal[
    "unlawful", "defamatory", "threat", "spam", "scam", "malware", "copyright", "impersonating", "privacy", "other"
]

SourceFormat = Literal["plain-text", "html", "markdown", "application"]

StoryType = Literal[
    "asked-to-friend", "asked-to-subscribe", "blocked-user", "blocked-user-in-posting", "comment-added",
    "comment-media-reaction-added-negative", "comment-media-reaction-added-positive", "comment-media-reaction-failed",
    "comment-post-task-failed", "comment-reaction-added-negative", "comment-reaction-added-positive",
    "comment-reaction-task-failed", "comment-update-task-failed", "defrosting", "friend-added", "friend-deleted",
    "friend-group-deleted", "mention-comment", "mention-posting", "posting-added",
    "posting-media-reaction-added-negative", "posting-media-reaction-added-positive", "posting-media-reaction-failed",
    "posting-post-task-failed", "posting-reaction-task-failed", "posting-subscribe-task-failed",
    "posting-update-task-failed", "posting-updated", "reaction-added-negative", "reaction-added-positive",
    "remote-comment-added", "reply-comment", "sheriff-complaint-added", "sheriff-complaint-decided", "sheriff-marked",
    "sheriff-unmarked", "subscriber-added", "subscriber-deleted", "unblocked-user", "unblocked-user-in-posting"
]

SubscriptionReason = Literal["user", "mention", "comment"]

SubscriptionType = Literal["feed", "posting", "posting-comments", "profile", "user-list"]

VerificationStatus = Literal["running", "correct", "incorrect", "error"]


class CommentOperations(Structure):
    view: PrincipalValue | None = None
    """view the comment"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """view the comment (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"
    edit: PrincipalValue | None = None
    """edit the comment"""

    @property
    def edit_or_default(self) -> PrincipalValue:
        """edit the comment (this property always returns default value instead of ``None``)"""
        return self.edit if self.edit is not None else "owner"
    delete: PrincipalValue | None = None
    """delete the comment"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """delete the comment (this property always returns default value instead of ``None``)"""
        return self.delete if self.delete is not None else "private"
    view_reactions: PrincipalValue | None = None
    """view the comment's reactions"""

    @property
    def view_reactions_or_default(self) -> PrincipalValue:
        """view the comment's reactions (this property always returns default value instead of ``None``)"""
        return self.view_reactions if self.view_reactions is not None else "public"
    view_negative_reactions: PrincipalValue | None = None
    """view the comment's negative reactions"""

    @property
    def view_negative_reactions_or_default(self) -> PrincipalValue:
        """view the comment's negative reactions (this property always returns default value instead of ``None``)"""
        return self.view_negative_reactions if self.view_negative_reactions is not None else "public"
    view_reaction_totals: PrincipalValue | None = None
    """view the number of the comment's reactions"""

    @property
    def view_reaction_totals_or_default(self) -> PrincipalValue:
        """
        view the number of the comment's reactions (this property always returns default value instead of ``None``)
        """
        return self.view_reaction_totals if self.view_reaction_totals is not None else "public"
    view_negative_reaction_totals: PrincipalValue | None = None
    """view the number of the comment's negative reactions"""

    @property
    def view_negative_reaction_totals_or_default(self) -> PrincipalValue:
        """
        view the number of the comment's negative reactions (this property always returns default value instead of
        ``None``)
        """
        return self.view_negative_reaction_totals if self.view_negative_reaction_totals is not None else "public"
    view_reaction_ratios: PrincipalValue | None = None
    """view the relative number of different types of the comment's reactions"""

    @property
    def view_reaction_ratios_or_default(self) -> PrincipalValue:
        """
        view the relative number of different types of the comment's reactions (this property always returns default
        value instead of ``None``)
        """
        return self.view_reaction_ratios if self.view_reaction_ratios is not None else "public"
    view_negative_reaction_ratios: PrincipalValue | None = None
    """view the relative number of different types of the comment's negative reactions"""

    @property
    def view_negative_reaction_ratios_or_default(self) -> PrincipalValue:
        """
        view the relative number of different types of the comment's negative reactions (this property always returns
        default value instead of ``None``)
        """
        return self.view_negative_reaction_ratios if self.view_negative_reaction_ratios is not None else "public"
    add_reaction: PrincipalValue | None = None
    """add a reaction to the comment"""

    @property
    def add_reaction_or_default(self) -> PrincipalValue:
        """add a reaction to the comment (this property always returns default value instead of ``None``)"""
        return self.add_reaction if self.add_reaction is not None else "signed"
    add_negative_reaction: PrincipalValue | None = None
    """add a negative reaction to the comment"""

    @property
    def add_negative_reaction_or_default(self) -> PrincipalValue:
        """add a negative reaction to the comment (this property always returns default value instead of ``None``)"""
        return self.add_negative_reaction if self.add_negative_reaction is not None else "signed"


class ContactOperations(Structure):
    view_feed_subscriber: PrincipalValue | None = None
    """see the subscriber information"""

    @property
    def view_feed_subscriber_or_default(self) -> PrincipalValue:
        """see the subscriber information (this property always returns default value instead of ``None``)"""
        return self.view_feed_subscriber if self.view_feed_subscriber is not None else "public"
    view_feed_subscription: PrincipalValue | None = None
    """see the subscription information"""

    @property
    def view_feed_subscription_or_default(self) -> PrincipalValue:
        """see the subscription information (this property always returns default value instead of ``None``)"""
        return self.view_feed_subscription if self.view_feed_subscription is not None else "public"
    view_friend: PrincipalValue | None = None
    """see the friend information"""

    @property
    def view_friend_or_default(self) -> PrincipalValue:
        """see the friend information (this property always returns default value instead of ``None``)"""
        return self.view_friend if self.view_friend is not None else "public"
    view_friend_of: PrincipalValue | None = None
    """see the friend-of information (this operation can be modified by admin only)"""

    @property
    def view_friend_of_or_default(self) -> PrincipalValue:
        """
        see the friend-of information (this operation can be modified by admin only) (this property always returns
        default value instead of ``None``)
        """
        return self.view_friend_of if self.view_friend_of is not None else "public"
    view_block: PrincipalValue | None = None
    """see the blocking information (this operation can be modified by admin only)"""

    @property
    def view_block_or_default(self) -> PrincipalValue:
        """
        see the blocking information (this operation can be modified by admin only) (this property always returns
        default value instead of ``None``)
        """
        return self.view_block if self.view_block is not None else "public"
    view_block_by: PrincipalValue | None = None
    """see the blocked-by information (this operation can be modified by admin only)"""

    @property
    def view_block_by_or_default(self) -> PrincipalValue:
        """
        see the blocked-by information (this operation can be modified by admin only) (this property always returns
        default value instead of ``None``)
        """
        return self.view_block_by if self.view_block_by is not None else "public"


class FeedOperations(Structure):
    add: PrincipalValue | None = None
    """add stories to the feed"""

    @property
    def add_or_default(self) -> PrincipalValue:
        """add stories to the feed (this property always returns default value instead of ``None``)"""
        return self.add if self.add is not None else "None"


class FriendOperations(Structure):
    view: PrincipalValue | None = None
    """view the membership of the node in the group of friends"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """
        view the membership of the node in the group of friends (this property always returns default value instead of
        ``None``)
        """
        return self.view if self.view is not None else "public"


class FriendGroupOperations(Structure):
    view: PrincipalValue | None = None
    """view the group of friends"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """view the group of friends (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"


class NodeNameOperations(Structure):
    manage: PrincipalValue | None = None
    """any modification of the node name, prolonging it etc."""

    @property
    def manage_or_default(self) -> PrincipalValue:
        """
        any modification of the node name, prolonging it etc. (this property always returns default value instead of
        ``None``)
        """
        return self.manage if self.manage is not None else "None"


class PeopleOperations(Structure):
    view_subscribers: PrincipalValue | None = None
    """view the list of subscribers"""

    @property
    def view_subscribers_or_default(self) -> PrincipalValue:
        """view the list of subscribers (this property always returns default value instead of ``None``)"""
        return self.view_subscribers if self.view_subscribers is not None else "public"
    view_subscriptions: PrincipalValue | None = None
    """view the list of subscriptions"""

    @property
    def view_subscriptions_or_default(self) -> PrincipalValue:
        """view the list of subscriptions (this property always returns default value instead of ``None``)"""
        return self.view_subscriptions if self.view_subscriptions is not None else "public"
    view_friends: PrincipalValue | None = None
    """view the list of friends"""

    @property
    def view_friends_or_default(self) -> PrincipalValue:
        """view the list of friends (this property always returns default value instead of ``None``)"""
        return self.view_friends if self.view_friends is not None else "public"
    view_friend_ofs: PrincipalValue | None = None
    """view the list of those who added this node to friends"""

    @property
    def view_friend_ofs_or_default(self) -> PrincipalValue:
        """
        view the list of those who added this node to friends (this property always returns default value instead of
        ``None``)
        """
        return self.view_friend_ofs if self.view_friend_ofs is not None else "public"
    view_blocked: PrincipalValue | None = None
    """view the list of blocked nodes"""

    @property
    def view_blocked_or_default(self) -> PrincipalValue:
        """view the list of blocked nodes (this property always returns default value instead of ``None``)"""
        return self.view_blocked if self.view_blocked is not None else "public"
    view_blocked_by: PrincipalValue | None = None
    """view the list of those who blocked this node"""

    @property
    def view_blocked_by_or_default(self) -> PrincipalValue:
        """
        view the list of those who blocked this node (this property always returns default value instead of ``None``)
        """
        return self.view_blocked_by if self.view_blocked_by is not None else "admin"
    view_subscribers_total: PrincipalValue | None = None
    """view the number of subscribers"""

    @property
    def view_subscribers_total_or_default(self) -> PrincipalValue:
        """view the number of subscribers (this property always returns default value instead of ``None``)"""
        return self.view_subscribers_total if self.view_subscribers_total is not None else "public"
    view_subscriptions_total: PrincipalValue | None = None
    """view the number of subscriptions"""

    @property
    def view_subscriptions_total_or_default(self) -> PrincipalValue:
        """view the number of subscriptions (this property always returns default value instead of ``None``)"""
        return self.view_subscriptions_total if self.view_subscriptions_total is not None else "public"
    view_friends_total: PrincipalValue | None = None
    """view the number of friends"""

    @property
    def view_friends_total_or_default(self) -> PrincipalValue:
        """view the number of friends (this property always returns default value instead of ``None``)"""
        return self.view_friends_total if self.view_friends_total is not None else "public"
    view_friend_ofs_total: PrincipalValue | None = None
    """view the number of those who added this node to friends"""

    @property
    def view_friend_ofs_total_or_default(self) -> PrincipalValue:
        """
        view the number of those who added this node to friends (this property always returns default value instead of
        ``None``)
        """
        return self.view_friend_ofs_total if self.view_friend_ofs_total is not None else "public"


class PostingOperations(Structure):
    view: PrincipalValue | None = None
    """view the posting"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """view the posting (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"
    edit: PrincipalValue | None = None
    """edit the posting"""

    @property
    def edit_or_default(self) -> PrincipalValue:
        """edit the posting (this property always returns default value instead of ``None``)"""
        return self.edit if self.edit is not None else "owner"
    delete: PrincipalValue | None = None
    """delete the posting"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """delete the posting (this property always returns default value instead of ``None``)"""
        return self.delete if self.delete is not None else "private"
    view_comments: PrincipalValue | None = None
    """view the posting's comments"""

    @property
    def view_comments_or_default(self) -> PrincipalValue:
        """view the posting's comments (this property always returns default value instead of ``None``)"""
        return self.view_comments if self.view_comments is not None else "public"
    add_comment: PrincipalValue | None = None
    """add a comment to the posting"""

    @property
    def add_comment_or_default(self) -> PrincipalValue:
        """add a comment to the posting (this property always returns default value instead of ``None``)"""
        return self.add_comment if self.add_comment is not None else "signed"
    override_comment: PrincipalValue | None = None
    """override the permissions of the posting's comments"""

    @property
    def override_comment_or_default(self) -> PrincipalValue:
        """
        override the permissions of the posting's comments (this property always returns default value instead of
        ``None``)
        """
        return self.override_comment if self.override_comment is not None else "owner"
    view_reactions: PrincipalValue | None = None
    """view the posting's reactions"""

    @property
    def view_reactions_or_default(self) -> PrincipalValue:
        """view the posting's reactions (this property always returns default value instead of ``None``)"""
        return self.view_reactions if self.view_reactions is not None else "public"
    view_negative_reactions: PrincipalValue | None = None
    """view the posting's negative reactions"""

    @property
    def view_negative_reactions_or_default(self) -> PrincipalValue:
        """view the posting's negative reactions (this property always returns default value instead of ``None``)"""
        return self.view_negative_reactions if self.view_negative_reactions is not None else "public"
    view_reaction_totals: PrincipalValue | None = None
    """view the number of the posting's reactions"""

    @property
    def view_reaction_totals_or_default(self) -> PrincipalValue:
        """
        view the number of the posting's reactions (this property always returns default value instead of ``None``)
        """
        return self.view_reaction_totals if self.view_reaction_totals is not None else "public"
    view_negative_reaction_totals: PrincipalValue | None = None
    """view the number of the posting's negative reactions"""

    @property
    def view_negative_reaction_totals_or_default(self) -> PrincipalValue:
        """
        view the number of the posting's negative reactions (this property always returns default value instead of
        ``None``)
        """
        return self.view_negative_reaction_totals if self.view_negative_reaction_totals is not None else "public"
    view_reaction_ratios: PrincipalValue | None = None
    """view the relative number of different types of the posting's reactions"""

    @property
    def view_reaction_ratios_or_default(self) -> PrincipalValue:
        """
        view the relative number of different types of the posting's reactions (this property always returns default
        value instead of ``None``)
        """
        return self.view_reaction_ratios if self.view_reaction_ratios is not None else "public"
    view_negative_reaction_ratios: PrincipalValue | None = None
    """view the relative number of different types of the posting's negative reactions"""

    @property
    def view_negative_reaction_ratios_or_default(self) -> PrincipalValue:
        """
        view the relative number of different types of the posting's negative reactions (this property always returns
        default value instead of ``None``)
        """
        return self.view_negative_reaction_ratios if self.view_negative_reaction_ratios is not None else "public"
    add_reaction: PrincipalValue | None = None
    """add a reaction to the posting"""

    @property
    def add_reaction_or_default(self) -> PrincipalValue:
        """add a reaction to the posting (this property always returns default value instead of ``None``)"""
        return self.add_reaction if self.add_reaction is not None else "signed"
    add_negative_reaction: PrincipalValue | None = None
    """add a negative reaction to the posting"""

    @property
    def add_negative_reaction_or_default(self) -> PrincipalValue:
        """add a negative reaction to the posting (this property always returns default value instead of ``None``)"""
        return self.add_negative_reaction if self.add_negative_reaction is not None else "signed"
    override_reaction: PrincipalValue | None = None
    """override the permissions of the posting's reactions"""

    @property
    def override_reaction_or_default(self) -> PrincipalValue:
        """
        override the permissions of the posting's reactions (this property always returns default value instead of
        ``None``)
        """
        return self.override_reaction if self.override_reaction is not None else "owner"
    override_comment_reaction: PrincipalValue | None = None
    """override the permissions of the posting's comment's reactions"""

    @property
    def override_comment_reaction_or_default(self) -> PrincipalValue:
        """
        override the permissions of the posting's comment's reactions (this property always returns default value
        instead of ``None``)
        """
        return self.override_comment_reaction if self.override_comment_reaction is not None else "owner"


class PrivateMediaFileOperations(Structure):
    view: PrincipalValue | None = None
    """view the media file"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """view the media file (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"


class ProfileOperations(Structure):
    edit: PrincipalValue | None = None
    """change the profile"""

    @property
    def edit_or_default(self) -> PrincipalValue:
        """change the profile (this property always returns default value instead of ``None``)"""
        return self.edit if self.edit is not None else "None"
    view_email: PrincipalValue | None = None
    """view the e-mail address in the profile"""

    @property
    def view_email_or_default(self) -> PrincipalValue:
        """view the e-mail address in the profile (this property always returns default value instead of ``None``)"""
        return self.view_email if self.view_email is not None else "None"


class ReactionOperations(Structure):
    view: PrincipalValue | None = None
    """view the reaction"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """view the reaction (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"
    delete: PrincipalValue | None = None
    """delete the reaction"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """delete the reaction (this property always returns default value instead of ``None``)"""
        return self.delete if self.delete is not None else "private"


class StoryOperations(Structure):
    edit: PrincipalValue | None = None
    """update the story"""

    @property
    def edit_or_default(self) -> PrincipalValue:
        """update the story (this property always returns default value instead of ``None``)"""
        return self.edit if self.edit is not None else "admin"
    delete: PrincipalValue | None = None
    """delete the story"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """delete the story (this property always returns default value instead of ``None``)"""
        return self.delete if self.delete is not None else "admin"


class SubscriberOperations(Structure):
    view: PrincipalValue | None = None
    """see the subscriber"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """see the subscriber (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"
    delete: PrincipalValue | None = None
    """delete the subscriber (this operation cannot be modified or overridden)"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """
        delete the subscriber (this operation cannot be modified or overridden) (this property always returns default
        value instead of ``None``)
        """
        return self.delete if self.delete is not None else "private"


class SubscriptionOperations(Structure):
    view: PrincipalValue | None = None
    """see the subscription"""

    @property
    def view_or_default(self) -> PrincipalValue:
        """see the subscription (this property always returns default value instead of ``None``)"""
        return self.view if self.view is not None else "public"
    delete: PrincipalValue | None = None
    """delete the subscription (this operation cannot be modified or overridden)"""

    @property
    def delete_or_default(self) -> PrincipalValue:
        """
        delete the subscription (this operation cannot be modified or overridden) (this property always returns default
        value instead of ``None``)
        """
        return self.delete if self.delete is not None else "admin"


class AcceptedReactions(Structure):
    positive: str
    """
    comma-separated list of codes of the positive reactions that are accepted; a code may be prefixed by ``0x`` to
    designate hexadecimal number and ``+`` to designate a recommended reaction
    """
    negative: str
    """
    comma-separated list of codes of the negative reactions that are accepted (the format is the same as above)
    """


class AskDescription(Structure):
    subject: AskSubject
    """request subject"""
    friend_group_id: str | None = None
    """
    if the request is to add this node to friends, this field contains ID of the corresponding group of friends on the
    remote node
    """
    message: str | None = None
    """message to the node admin"""


class AsyncOperationCreated(Structure):
    id: str
    """ID of the asynchronous operation that was created"""


class AvatarAttributes(Structure):
    media_id: str
    """ID of the public media file used as a source image"""
    clip_x: int
    """x coordinate of the top-left corner of the clipping square"""
    clip_y: int
    """y coordinate of the top-left corner of the clipping square"""
    clip_size: int
    """size of the clipping square"""
    avatar_size: int
    """size of the avatar to be created"""
    rotate: float
    """rotation angle of the source image"""
    shape: str | None = None
    """shape of the avatar"""
    ordinal: int | None = None
    """ordinal of the avatar"""


class AvatarDescription(Structure):
    media_id: str
    """ID of the public media file used as an avatar image"""
    shape: str
    """shape of the avatar"""
    optional: bool | None = None
    """
    if set to ``True``, the node will ignore the absence of the media file referenced in ``mediaId`` field (empty
    avatar will be used in this case); if set to ``False`` or absent, the node will return an error, if the media file
    referenced in ``mediaId`` field is absent
    """


class AvatarImage(Structure):
    media_id: str
    """ID of the media file"""
    path: str
    """virtual location of the media file, relative to the ``/media`` virtual page"""
    width: int | None = None
    """width of the media in pixels (``None``, if the media file is not an image/video)"""
    height: int | None = None
    """height of the media in pixels (``None``, if the media file is not an image/video)"""
    shape: str | None = None
    """shape of the avatar"""


class AvatarInfo(Structure):
    id: str
    """ID of the avatar"""
    media_id: str
    """ID of the media file"""
    path: str
    """virtual location of the media file, relative to the ``/media`` virtual page"""
    width: int | None = None
    """width of the media in pixels (``None``, if the media file is not an image/video)"""
    height: int | None = None
    """height of the media in pixels (``None``, if the media file is not an image/video)"""
    shape: str | None = None
    """shape of the avatar"""
    ordinal: int
    """ordinal of the avatar"""


class AvatarOrdinal(Structure):
    id: str
    """ID of the avatar"""
    ordinal: int
    """ordinal of the avatar"""


class AvatarsOrdered(Structure):
    ids: List[str]
    """IDs of avatars"""


class BlockedInstantAttributes(Structure):
    story_type: StoryType
    """type of the story"""
    entry_id: str | None = None
    """ID of the local entry the blocked story should be related to"""
    remote_node_name: str | None = None
    """node name of the remote posting the blocked story should be related to"""
    remote_posting_id: str | None = None
    """ID of the remote posting the blocked story should be related to"""
    remote_owner_name: str | None = None
    """owner name of the remote object the blocked story should be related to"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the story will be unblocked; ``None`` or absent, if the story is blocked
    permanently
    """


class BlockedInstantFilter(Structure):
    story_type: StoryType
    """type of the story"""
    entry_id: str | None = None
    """ID of the local entry the blocked story should be related to"""
    remote_node_name: str | None = None
    """node name of the remote posting the blocked story should be related to"""
    remote_posting_id: str | None = None
    """ID of the remote posting the blocked story should be related to"""
    remote_owner_name: str | None = None
    """owner name of the remote object the blocked story should be related to"""


class BlockedInstantInfo(Structure):
    id: str
    story_type: StoryType
    """type of the story"""
    entry_id: str | None = None
    """ID of the local entry the blocked story should be related to"""
    remote_node_name: str | None = None
    """node name of the remote posting the blocked story should be related to"""
    remote_posting_id: str | None = None
    """ID of the remote posting the blocked story should be related to"""
    remote_owner_name: str | None = None
    """owner name of the remote object the blocked story should be related to"""
    created_at: Timestamp
    """blocking timestamp - the real time when the story was blocked"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the story will be unblocked; ``None`` or absent, if the story is blocked
    permanently
    """


class BlockedPostingInstantInfo(Structure):
    id: str
    story_type: StoryType
    """type of the story"""
    remote_owner_name: str | None = None
    """owner name of the remote object the blocked story should be related to"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the story will be unblocked; ``None`` or absent, if the story is blocked
    permanently
    """


class BlockedUserAttributes(Structure):
    blocked_operation: BlockedOperation
    """operation that is to be blocked"""
    node_name: str
    """name of the blocked node"""
    entry_id: str | None = None
    """ID of the local entry, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    entry_node_name: str | None = None
    """
    node name of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally
    """
    entry_posting_id: str | None = None
    """ID of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the node will be unblocked; ``None`` or absent, if the node is blocked
    permanently
    """
    reason_src: str | None = None
    """source text of the reason of blocking"""
    reason_src_format: SourceFormat | None = None
    """
    format of the source text of the reason of blocking, the list of available formats is returned in
    ``PostingFeatures``
    """


class BlockedUserFilter(Structure):
    blocked_operations: List[BlockedOperation] | None = None
    """operations that are blocked"""
    node_name: str | None = None
    """name of the blocked node"""
    entry_id: str | None = None
    """ID of the local entry, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    entry_node_name: str | None = None
    """
    node name of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally
    """
    entry_posting_id: str | None = None
    """ID of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    strict: bool | None = None
    """
    if set to ``True``, only the blockings that strictly fit the criteria are returned; otherwise global blockings are
    returned even if the search is limited to a particular posting
    """


class BlockedUsersChecksums(Structure):
    visibility: int
    """checksum of the list of users that are hidden"""


class CarteInfo(Structure):
    carte: str
    beginning: Timestamp
    """timestamp of the beginning of the carte's life"""
    deadline: Timestamp
    """timestamp of the end of the carte's life"""
    permissions: List[str] | None = None
    """
    the list of permissions granted to the carte; the possible values are:
    
    * ``other`` - any other permission not listed below;
    * ``view-media`` - view media files.
    """


class CarteSet(Structure):
    cartes_ip: str | None = None
    """the client IP address the cartes are bound to"""
    cartes: List[CarteInfo]
    """the cartes"""
    created_at: Timestamp
    """cartes creation timestamp"""


class ClientReactionInfo(Structure):
    negative: bool
    """``True``, if the reaction is negative, ``False``, if positive"""
    emoji: int
    """reaction code, usually interpreted by clients as emoji code point"""
    created_at: Timestamp
    """reaction creation timestamp - the real time when the reaction was created"""
    deadline: Timestamp | None = None
    """if present, the reaction will be erased at this time"""


class CommentMassAttributes(Structure):
    senior_operations: CommentOperations | None = None
    """the operations and the corresponding principals that are overridden by the comment's owner ("senior")"""


class CommentTotalInfo(Structure):
    total: int
    """total number of comments in the posting after the operation"""


class ContactInfo(Structure):
    node_name: str
    full_name: str | None = None
    gender: str | None = None
    avatar: AvatarImage | None = None
    closeness: float
    """
    closeness of the contact to the node, which is calculated from the number of reactions and comments and their age
    """
    has_feed_subscriber: bool | None = None
    """the contact is subscribed to at least one of the node's feeds"""
    has_feed_subscription: bool | None = None
    """the node is subscribed to at least one of the contact's feeds"""
    has_friend: bool | None = None
    """the contact is a friend of the node"""
    has_friend_of: bool | None = None
    """the node is a friend of the contact"""
    has_block: bool | None = None
    """the contact is blocked by the node"""
    has_block_by: bool | None = None
    """the node is blocked by the contact"""
    operations: ContactOperations | None = None
    """the supported operations and the corresponding principals"""
    owner_operations: ContactOperations | None = None
    """the supported operations and the corresponding principals as defined by the contact's owner"""
    admin_operations: ContactOperations | None = None
    """the operations and the corresponding principals that are overridden by the node administrator"""


class Credentials(Structure):
    login: str
    password: str


class CredentialsChange(Structure):
    token: str | None = None
    """credentials reset token"""
    old_password: str | None = None
    """the current password"""
    login: str
    password: str


class CredentialsCreated(Structure):
    created: bool
    """``True`` if the credentials are initialized already, ``False`` otherwise"""


class DeleteNodeStatus(Structure):
    requested: bool
    """``True`` if the request is sent, ``False`` otherwise"""


class DeleteNodeText(Structure):
    message: str | None = None
    """text message for the provider"""


class DomainAttributes(Structure):
    name: str | None = None
    """domain's hostname or ``_default_`` for the default domain"""
    node_id: str | None = None
    """domain's node ID"""


class DomainAvailable(Structure):
    name: str
    """fully-qualified domain name"""


class DomainInfo(Structure):
    name: str
    """domain's hostname or ``_default_`` for the default domain"""
    node_id: str
    """domain's node ID"""
    created_at: Timestamp
    """domain creation timestamp"""


class EmailHint(Structure):
    email_hint: str
    """
    a masked E-mail address that should help user to understand which E-mail address was used without revealing it
    """


class FeedReference(Structure):
    feed_name: str
    """name of the feed"""
    published_at: Timestamp
    """story publication timestamp - the time the story is published under in the feed"""
    pinned: bool | None = None
    """
    ``True``, if the story is pinned (should appear before any non-pinned story in the feed), ``False`` otherwise
    """
    moment: int
    story_id: str
    """ID of the story"""
    operations: StoryOperations | None = None
    """the supported operations and the corresponding principals for the story in the feed"""


class FeedStatus(Structure):
    total: int
    """total number of stories"""
    total_pinned: int
    """total number of pinned stories"""
    last_moment: int | None = None
    """moment of the most recent story"""
    not_viewed: int | None = None
    """number of stories that have not been viewed yet, admin only"""
    not_read: int | None = None
    """number of stories that have not been read yet, admin only"""
    not_viewed_moment: int | None = None
    """moment of the oldest non-viewed story, admin only"""
    not_read_moment: int | None = None
    """moment of the oldest non-read story, admin only"""


class FeedStatusChange(Structure):
    viewed: bool | None = None
    """new value of the ``viewed`` flag (``None``, if the flag is not changed)"""
    read: bool | None = None
    """new value of the ``read`` flag (``None``, if the flag is not changed)"""
    before: int
    """change flags for all stories before this moment, inclusive"""


class FeedWithStatus(Structure):
    feed_name: str
    """name of the feed"""
    not_viewed: int
    """number of stories in the feed that have not been viewed yet"""
    not_read: int
    """number of stories in the feed that have not been read yet"""


class FriendGroupAssignment(Structure):
    id: str
    """ID of the group of friends"""
    operations: FriendOperations | None = None
    """the operations and the corresponding principals"""


class FriendGroupDescription(Structure):
    title: str
    """title of the group of friends"""
    operations: FriendGroupOperations | None = None
    """the operations and the corresponding principals"""


class FriendGroupDetails(Structure):
    id: str
    """ID of the group of friends"""
    title: str | None = None
    """title of the group of friends"""
    added_at: Timestamp
    """the friendship timestamp - the real time when the node was added to the group of friends"""
    operations: FriendOperations | None = None
    """list of the supported operations and the corresponding principals"""


class FriendGroupInfo(Structure):
    id: str
    title: str | None = None
    """title of the group of friends"""
    created_at: Timestamp
    """the group creation timestamp - the real time when the group of friends was created"""
    operations: FriendGroupOperations | None = None
    """list of the supported operations and the corresponding principals"""


class FriendGroupsFeatures(Structure):
    available: List[FriendGroupInfo]
    """list of groups of friends existing on the node"""
    member_of: List[FriendGroupDetails] | None = None
    """list of groups of friends the client is member of"""


class FriendInfo(Structure):
    node_name: str
    """name of the node"""
    contact: ContactInfo | None = None
    """information about the node"""
    groups: List[FriendGroupDetails] | None = None
    """groups of friends the node belongs to"""


class FriendOfInfo(Structure):
    remote_node_name: str
    """name of the remote node"""
    contact: ContactInfo | None = None
    """information about the remote node"""
    groups: List[FriendGroupDetails] | None = None
    """groups of friends on the remote node this node was added to"""


class FundraiserInfo(Structure):
    title: str
    """fundraiser title"""
    qr_code: str | None = None
    """text or URI to be encoded and displayed as QR-code"""
    text: str | None = None
    """arbitrary text to be displayed"""
    href: str | None = None
    """link to the fundraiser"""


class LinkPreview(Structure):
    site_name: str | None = None
    """name of the site"""
    url: str | None = None
    """canonical URL of the page"""
    title: str | None = None
    """title of the page"""
    description: str | None = None
    """description of the page"""
    image_hash: str | None = None
    """hash of the image presenting the page"""


class LinkPreviewInfo(Structure):
    site_name: str | None = None
    """name of the site"""
    url: str | None = None
    """canonical URL of the page"""
    title: str | None = None
    """title of the page"""
    description: str | None = None
    """description of the page"""
    image_url: str | None = None
    """URL of the image presenting the page"""


class MediaFilePreviewInfo(Structure):
    target_width: int
    """the width the preview was prepared for viewing at"""
    direct_path: str | None = None
    """
    location of the media file, relative to the ``/media``; points to a static image served directly from a filesystem;
    static images do not accept any query parameters including authentication parameters
    """
    width: int
    """actual width of the preview in pixels"""
    height: int
    """actual height of the preview in pixels"""
    original: bool | None = None
    """``True`` if the preview is identical to the original media, ``False`` otherwise"""


class MediaWithDigest(Structure):
    id: str
    """ID of the media file"""
    digest: str | None = None
    """cryptographic digest of the media file"""


class NameToRegister(Structure):
    name: str


class NotificationPacket(Structure):
    id: str
    """ID of the notification packet on the sending node (used to filter out duplicates)"""
    node_name: str
    """name of the sending node"""
    full_name: str | None = None
    """full name of the sending node"""
    gender: str | None = None
    """gender of the sending node"""
    avatar: AvatarImage | None = None
    """avatar of the sending node"""
    created_at: Timestamp
    """notification packet creation timestamp"""
    type: str
    """notification type"""
    notification: str
    """the notification, a string representation of a JSON structure (see Notifications page for details)"""
    signature: bytes
    """the notification packet sender signature (use ``NotificationPacket`` fingerprint)"""
    signature_version: int
    """signature version (i.e. fingerprint version)"""


class NodeNameInfo(Structure):
    name: str | None = None
    operation_status: OperationStatus | None = None
    """status of the latest operation with the node name"""
    operation_status_updated: Timestamp | None = None
    """the last time the operation status was updated"""
    operation_error_code: str | None = None
    """if the operation with the node name was failed, the code of the failure"""
    operation_error_message: str | None = None
    """if the operation with the node name was failed, the human-readable description of the failure"""
    operations: NodeNameOperations | None = None
    """the supported operations and the corresponding principals"""


class PeopleGeneralInfo(Structure):
    feed_subscribers_total: int | None = None
    """total number of subscribers of the node"""
    feed_subscriptions_total: int | None = None
    """total number of subscriptions of the node"""
    friends_total: Mapping[str, int] | None = None
    """total number of friends in every group"""
    friend_ofs_total: int | None = None
    """total number of nodes that added this node to their friends"""
    blocked_total: int | None = None
    """total number of blocked nodes"""
    blocked_by_total: int | None = None
    """total number of nodes that blocked this node"""
    operations: PeopleOperations | None = None
    """the supported operations and the corresponding principals"""


class PluginContext(Structure):
    root_admin: bool
    """``True``, if the client has authenticated as root admin, ``False`` otherwise"""
    admin: bool
    """``True``, if the client has authenticated as node admin, ``False`` otherwise"""
    auth_categories: List[str]
    """
    the list of permissions granted to the client, if it has authenticated as node admin; see ``TokenInfo.permissions``
    for the list of possible values
    """
    client_name: str
    """node name of the client"""
    remote_address: str
    """IP address of the client"""
    user_agent: str
    """user agent (browser) used by the client"""
    user_agent_os: str
    """operating system used by the client"""
    node_id: str
    """ID of the current node"""
    node_name: str
    """node name of the current node"""
    domain_name: str
    """domain name of the current node"""
    origin_url: str
    """full URL of the request"""


class PostingFeatures(Structure):
    post: bool | None = None
    """``True`` if the client is allowed to create postings, ``False`` otherwise"""
    subject_present: bool
    """``True`` if new postings are recommended to have a subject, ``False`` otherwise"""
    source_formats: List[SourceFormat]
    """list of source text formats the node understands"""
    media_max_size: int
    """maximal size of a media attachment in a post"""
    image_recommended_size: int
    """maximal size of a compressed image in a post"""
    image_recommended_pixels: int
    """maximal resolution of a compressed image in a post (in pixels)"""
    image_formats: List[str]
    """list of image formats (in MIME type form) the node understands"""


class PostingSourceInfo(Structure):
    node_name: str
    """name of the remote node"""
    full_name: str | None = None
    """full name of the remote node"""
    avatar: AvatarImage | None = None
    """avatar of the remote node"""
    feed_name: str
    """name of the feed on the remote node"""
    posting_id: str
    """ID of the posting on the remote node"""
    created_at: Timestamp
    """timestamp when the posting was received from this source"""


class PrivateMediaFileInfo(Structure):
    id: str
    """ID of the media file"""
    hash: str
    """SHA-1 hash of the media file"""
    path: str
    """virtual location of the media file, relative to the ``/media`` virtual page"""
    direct_path: str | None = None
    """
    location of the media file, relative to the ``/media``; points to a static image served directly from a filesystem;
    static images do not accept any query parameters including authentication parameters
    """
    mime_type: str
    """MIME type of the media"""
    width: int | None = None
    """width of the media in pixels (``None``, if the media file is not an image or video)"""
    height: int | None = None
    """height of the media in pixels (``None``, if the media file is not an image or video)"""
    orientation: int | None = None
    """
    media orientation, the value should be interpreted like the orientation value present in JPEG EXIF data (``None``,
    if the media file is not an image or video)
    """
    size: int
    """size of the media file in bytes"""
    posting_id: str | None = None
    """ID of the posting linked to the media"""
    previews: List[MediaFilePreviewInfo] | None = None
    """list of media previews - downscaled versions of the media"""
    operations: PrivateMediaFileOperations | None = None
    """the supported operations and the corresponding principals"""


class ProfileAttributes(Structure):
    full_name: str | None = None
    """node owner's full name"""
    gender: str | None = None
    """node owner's gender"""
    email: str | None = None
    """node owner's E-mail address"""
    title: str | None = None
    """node title"""
    bio_src: str | None = None
    """the source text of node owner's bio (arbitrary text)"""
    bio_src_format: SourceFormat | None = None
    """
    format of the source text of node owner's bio, ``markdown`` by default; the list of available formats is returned
    in ``PostingFeatures``
    """
    avatar_id: str | None = None
    """node owner's avatar ID"""
    fundraisers: List[FundraiserInfo] | None = None
    """list of fundraisers - methods of giving a donation to the node owner"""
    operations: ProfileOperations | None = None
    """the operations and the corresponding principals"""


class ProfileInfo(Structure):
    full_name: str | None = None
    """node owner's full name"""
    gender: str | None = None
    """node owner's gender"""
    email: str | None = None
    """node owner's E-mail address"""
    title: str | None = None
    """node title"""
    bio_src: str | None = None
    """the source text of node owner's bio (arbitrary text), may be absent if not requested"""
    bio_src_format: SourceFormat | None = None
    """
    format of the source text of node owner's bio, ``markdown`` by default, may be absent if not requested; the list of
    available formats is returned in ``PostingFeatures``
    """
    bio_html: str | None = None
    """HTML representation of node owner's bio"""
    avatar: AvatarInfo | None = None
    """node owner's avatar"""
    fundraisers: List[FundraiserInfo] | None = None
    """list of fundraisers - methods of giving a donation to the node owner"""
    operations: ProfileOperations | None = None
    """the supported operations and the corresponding principals"""


class PublicMediaFileInfo(Structure):
    id: str
    """ID of the media file"""
    path: str
    """virtual location of the media file, relative to the ``/media`` virtual page"""
    width: int | None = None
    """width of the media in pixels (``None``, if the media file is not an image or video)"""
    height: int | None = None
    """height of the media in pixels (``None``, if the media file is not an image or video)"""
    orientation: int | None = None
    """
    media orientation, the value should be interpreted like the orientation value present in JPEG EXIF data (``None``,
    if the media file is not an image or video)
    """
    size: int
    """size of the media file in bytes"""


class PushRelayClientAttributes(Structure):
    type: PushRelayType
    """type of the relay"""
    client_id: str
    """ID/token of the client"""
    lang: str | None = None
    """language of the messages"""


class ReactionAttributes(Structure):
    negative: bool
    """``True``, if the reaction is negative, ``False``, if positive"""
    emoji: int
    """reaction code, usually interpreted by clients as emoji code point"""
    operations: ReactionOperations | None = None
    """the operations and the corresponding principals"""


class ReactionDescription(Structure):
    owner_name: str | None = None
    """reaction owner's node name"""
    owner_full_name: str | None = None
    """reaction owner's full name"""
    owner_gender: str | None = None
    """reaction owner's gender"""
    owner_avatar: AvatarDescription | None = None
    """reaction owner's avatar"""
    negative: bool
    """``True``, if the reaction is negative, ``False``, if positive"""
    emoji: int
    """reaction code, usually interpreted by clients as emoji code point"""
    signature: bytes | None = None
    """the reaction owner signature (use ``Reaction`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    operations: ReactionOperations | None = None
    """the operations and the corresponding principals"""


class ReactionsFilter(Structure):
    owner_name: str | None = None
    """reaction owner's name"""
    postings: List[str] | None = None
    """list of IDs of postings"""


class ReactionInfo(Structure):
    owner_name: str | None = None
    """reaction owner's node name"""
    owner_full_name: str | None = None
    """reaction owner's full name"""
    owner_gender: str | None = None
    """reaction owner's gender"""
    owner_avatar: AvatarImage | None = None
    """reaction owner's avatar"""
    posting_id: str | None = None
    """ID of the posting"""
    posting_revision_id: str | None = None
    """ID of the posting revision, if relevant"""
    comment_id: str | None = None
    """ID of the comment, if relevant"""
    comment_revision_id: str | None = None
    """ID of the comment revision, if relevant"""
    negative: bool | None = None
    """``True``, if the reaction is negative, ``False``, if positive"""
    emoji: int | None = None
    """reaction code, usually interpreted by clients as emoji code point"""
    moment: int | None = None
    created_at: Timestamp | None = None
    """reaction creation timestamp - the real time when the reaction was created"""
    deadline: Timestamp | None = None
    """if present, the reaction will be erased at this time"""
    signature: bytes | None = None
    """the reaction owner signature (use ``Reaction`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    operations: ReactionOperations | None = None
    """the supported operations and the corresponding principals"""
    owner_operations: ReactionOperations | None = None
    """the supported operations and the corresponding principals as defined by the reaction's owner"""
    senior_operations: ReactionOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the reaction's "senior": the posting's owner
    in the case of reaction to a posting or the comment's owner in the case of reaction to a comment
    """
    major_operations: ReactionOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the posting's owner ("major") in the case of
    reaction to a comment; not set in the case of reaction to a posting
    """


class ReactionsSliceInfo(Structure):
    before: int
    """the slice contains all reactions before this moment, inclusive. May be the far future."""
    after: int
    """the slice contains all reactions after this moment, exclusive. May be the far past."""
    total: int
    """total number of reactions in the whole list"""
    reactions: List[ReactionInfo]
    """the reactions"""


class ReactionTotalInfo(Structure):
    emoji: int
    """reaction code, usually interpreted by clients as emoji code point"""
    total: int | None = None
    """total number of reactions with the given code"""
    share: float | None = None
    """
    share the reactions with the given code stand from the total number of reactions (may be absent, if ``total`` is
    present)
    """


class ReactionTotalsFilter(Structure):
    postings: List[str]
    """list of IDs of postings"""


class ReactionTotalsInfo(Structure):
    entry_id: str
    """ID of the entry"""
    positive: List[ReactionTotalInfo] | None = None
    """summary of positive reactions"""
    negative: List[ReactionTotalInfo] | None = None
    """summary of negative reactions"""


class ReactionOverride(Structure):
    operations: ReactionOperations | None = None
    """the supported operations and the corresponding principals"""
    senior_operations: ReactionOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the reaction's "senior": the posting's owner
    in the case of reaction to a posting or the comment's owner in the case of reaction to a comment
    """
    major_operations: ReactionOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the posting's owner ("major") in the case of
    reaction to a comment; not set in the case of reaction to a posting
    """


class RegisteredNameSecret(Structure):
    name: str
    mnemonic: List[str] | None = None
    """human-friendly mnemonic of the updating key"""
    secret: str | None = None
    """base64-encoded secret of the updating key"""


class RemoteFeed(Structure):
    node_name: str
    """name of the node"""
    feed_name: str
    """name of the feed on the node"""


class RemoteMedia(Structure):
    id: str
    """ID of the media file"""
    hash: str | None = None
    """SHA-1 hash of the media file"""
    digest: str | None = None
    """cryptographic digest of the media file"""


class RemoteMediaInfo(Structure):
    id: str
    """ID of the media file"""
    hash: str | None = None
    """SHA-1 hash of the media file"""
    digest: str | None = None
    """cryptographic digest of the media file"""


class RemotePosting(Structure):
    node_name: str
    """name of the node"""
    posting_id: str
    """ID of the posting on the node"""


class RemotePostingOrNode(Structure):
    node_name: str
    """name of the node"""
    posting_id: str | None = None
    """ID of the posting on the node"""


class RemotePostingVerificationInfo(Structure):
    id: str
    """asynchronous operation ID"""
    node_name: str
    posting_id: str
    revision_id: str | None = None
    status: VerificationStatus | None = None
    """status of the operation"""
    error_code: str | None = None
    """error code"""
    error_message: str | None = None
    """human-readable error message"""


class RemoteReactionVerificationInfo(Structure):
    id: str
    """asynchronous operation ID"""
    node_name: str
    posting_id: str
    reaction_owner_name: str
    """node name of the reaction's owner"""
    status: VerificationStatus | None = None
    """status of the operation"""
    error_code: str | None = None
    """error code"""
    error_message: str | None = None
    """human-readable error message"""


class RepliedTo(Structure):
    id: str
    """ID of the comment"""
    revision_id: str | None = None
    """ID of the comment revision"""
    name: str
    """node name of the comment's owner"""
    full_name: str | None = None
    """full name of the comment's owner"""
    gender: str | None = None
    """gender of the comment's owner"""
    avatar: AvatarImage | None = None
    """avatar of the comment's owner"""
    heading: str | None = None
    """heading of the comment"""
    digest: bytes
    """cryptographic digest of the comment (use ``Comment`` fingerprint)"""


class Result(Structure):
    error_code: str
    """error code"""
    message: str | None = None
    """human-readable error message"""


class SheriffMark(Structure):
    sheriff_name: str
    """name of the sheriff that added the mark"""


class SettingInfo(Structure):
    name: str
    """name of the setting"""
    value: str | None = None
    """value of the setting"""


class SettingMetaAttributes(Structure):
    name: str
    """name of the setting"""
    default_value: str | None = None
    """default value of the setting (if absent or ``None``, the built-in default value will be used)"""
    privileged: bool | None = None
    """the setting should be privileged (if absent or ``None``, the built-in value of the flag will be used)"""


class SettingTypeModifiers(Structure):
    format: str | None = None
    """
    preferred format of displaying the value
    (``int``)
    
    * ``size`` - data size in bytes/kilobytes/megabytes etc.
    """
    min: str | None = None
    """(``int``, ``Duration``) minimal value"""
    max: str | None = None
    """(``int``, ``Duration``) maximal value"""
    multiline: bool | None = None
    """(``string``) ``True``, if the value is a multiline text"""
    never: bool | None = None
    """(``Duration``) ``True``, if value ``never`` is allowed"""
    always: bool | None = None
    """(``Duration``) ``True``, if value ``always`` is allowed"""
    principals: List[PrincipalFlag] | None = None
    """(``Principal``) list of allowed principals"""


class SheriffComplaintDecisionText(Structure):
    reject: bool
    """``True``, if the complaints in the group are to be rejected, ``False`` otherwise"""
    decision_code: SheriffOrderReason | None = None
    """the decision"""
    decision_details: str | None = None
    """detailed explanation of the decision in user-readable form"""
    anonymous: bool | None = None
    """``True``, if the complaints' owners' names are not to be published, ``False`` otherwise"""


class SheriffComplaintGroupInfo(Structure):
    id: str
    remote_node_name: str
    """name of the node the complaints are related to"""
    remote_node_full_name: str | None = None
    """full name of the node the complaints are related to"""
    remote_feed_name: str
    """name of the feed the complaints are related to"""
    remote_posting_id: str | None = None
    """ID of the posting the complaints are related to"""
    remote_posting_revision_id: str | None = None
    """ID of the posting's revision the complaints are related to"""
    remote_posting_owner_name: str | None = None
    """posting owner's node name"""
    remote_posting_owner_full_name: str | None = None
    """posting owner's full name"""
    remote_posting_owner_gender: str | None = None
    """posting owner's gender"""
    remote_posting_heading: str | None = None
    """heading of the posting"""
    remote_comment_id: str | None = None
    """ID of the comment the complaints are related to"""
    remote_comment_revision_id: str | None = None
    """ID of the comment's revision the complaints are related to"""
    remote_comment_owner_name: str | None = None
    """comment owner's node name"""
    remote_comment_owner_full_name: str | None = None
    """comment owner's full name"""
    remote_comment_owner_gender: str | None = None
    """comment owner's gender"""
    remote_comment_heading: str | None = None
    """heading of the comment"""
    created_at: Timestamp
    """the group of complaints creation timestamp - the real time when the group was created"""
    moment: int
    """moment of the group of complaints"""
    status: SheriffComplaintStatus
    """status of the group of complaints"""
    decision_code: SheriffOrderReason | None = None
    """sheriff's decision"""
    decision_details: str | None = None
    """detailed explanation of sheriff's decision in user-readable form"""
    decided_at: Timestamp | None = None
    """sheriff's decision timestamp - the real time when the decision was made"""
    anonymous: bool | None = None
    """``True``, if the complaints' owners' names are not published, ``False`` otherwise"""


class SheriffComplaintGroupsSliceInfo(Structure):
    before: int
    """the slice contains all groups before this moment, inclusive. May be the far future."""
    after: int
    """the slice contains all groups after this moment, exclusive. May be the far past."""
    groups: List[SheriffComplaintGroupInfo]
    """the groups"""
    total: int
    """total number of groups"""
    total_in_past: int
    """number of groups before this slice till the far past"""
    total_in_future: int
    """number of groups after this slice till the far future"""


class SheriffComplaintInfo(Structure):
    id: str
    owner_name: str
    """complaint owner's node name"""
    owner_full_name: str | None = None
    """complaint owner's full name"""
    owner_gender: str | None = None
    """complaint owner's gender"""
    group: SheriffComplaintGroupInfo | None = None
    """the group of complaints this complaint belongs to"""
    reason_code: SheriffOrderReason
    """reason of the complaint"""
    reason_details: str | None = None
    """detailed explanation of reason of the complaint in user-readable form"""
    anonymous_requested: bool | None = None
    """``True``, if the complaint's owner wants his name not to be published, ``False`` otherwise"""
    created_at: Timestamp
    """complaint creation timestamp - the real time when the order was created"""


class SheriffComplaintText(Structure):
    owner_full_name: str | None = None
    """complaint owner's full name"""
    owner_gender: str | None = None
    """complaint owner's gender"""
    node_name: str
    """name of the node the complaint is related to"""
    full_name: str | None = None
    """full name of the node the complaint is related to"""
    feed_name: str
    """name of the feed the complaint is related to"""
    posting_id: str | None = None
    """ID of the posting the complaint is related to"""
    posting_owner_name: str | None = None
    """posting owner's node name"""
    posting_owner_full_name: str | None = None
    """posting owner's full name"""
    posting_owner_gender: str | None = None
    """posting owner's gender"""
    posting_heading: str | None = None
    """heading of the posting"""
    comment_id: str | None = None
    """ID of the comment the complaint is related to"""
    comment_owner_name: str | None = None
    """comment owner's node name"""
    comment_owner_full_name: str | None = None
    """comment owner's full name"""
    comment_owner_gender: str | None = None
    """comment owner's gender"""
    comment_heading: str | None = None
    """heading of the comment"""
    reason_code: SheriffOrderReason | None = None
    """reason of the complaint"""
    reason_details: str | None = None
    """detailed explanation of reason of the complaint in user-readable form"""
    anonymous: bool | None = None
    """``True``, if the complaint's owner wants his name not to be published, ``False`` otherwise"""


class SheriffOrderAttributes(Structure):
    delete: bool | None = None
    """``True``, if the order is to cancel the previous order of this type, ``False`` otherwise"""
    feed_name: str
    """name of the feed the order is related to"""
    posting_id: str | None = None
    """ID of the posting the order is related to"""
    comment_id: str | None = None
    """ID of the comment the order is related to"""
    category: SheriffOrderCategory
    """category of the order"""
    reason_code: SheriffOrderReason | None = None
    """reason of the order"""
    reason_details: str | None = None
    """detailed explanation of reason of the order in user-readable form"""


class SheriffOrderDetails(Structure):
    id: str
    delete: bool | None = None
    """``True``, if the order is to cancel the previous order of this type, ``False`` otherwise"""
    sheriff_name: str
    """node name of the sheriff"""
    sheriff_avatar: AvatarDescription | None = None
    """sheriff's avatar"""
    feed_name: str
    """name of the feed the order is related to"""
    posting_id: str | None = None
    """ID of the posting the order is related to"""
    comment_id: str | None = None
    """ID of the comment the order is related to"""
    category: SheriffOrderCategory
    """category of the order"""
    reason_code: SheriffOrderReason | None = None
    """reason of the order"""
    reason_details: str | None = None
    """detailed explanation of reason of the order in user-readable form"""
    created_at: Timestamp
    """order creation timestamp - the real time when the order was created"""
    signature: bytes
    """the sheriff's signature (use ``SheriffOrder`` fingerprint)"""
    signature_version: int
    """signature version (i.e. fingerprint version)"""


class SheriffOrderInfo(Structure):
    id: str
    delete: bool | None = None
    """``True``, if the order is to cancel the previous order of this type, ``False`` otherwise"""
    sheriff_name: str
    """node name of the sheriff"""
    node_name: str
    """name of the node the order was sent to"""
    node_full_name: str | None = None
    """full name of the node the order was sent to"""
    feed_name: str
    """name of the feed the order is related to"""
    posting_id: str | None = None
    """ID of the posting the order is related to"""
    posting_revision_id: str | None = None
    """ID of the posting's revision the order is related to"""
    posting_owner_name: str | None = None
    """posting owner's node name"""
    posting_owner_full_name: str | None = None
    """posting owner's full name"""
    posting_owner_gender: str | None = None
    """posting owner's gender"""
    posting_heading: str | None = None
    """heading of the posting"""
    comment_id: str | None = None
    """ID of the comment the order is related to"""
    comment_revision_id: str | None = None
    """ID of the comment's revision the order is related to"""
    comment_owner_name: str | None = None
    """comment owner's node name"""
    comment_owner_full_name: str | None = None
    """comment owner's full name"""
    comment_owner_gender: str | None = None
    """comment owner's gender"""
    comment_heading: str | None = None
    """heading of the comment"""
    category: SheriffOrderCategory
    """category of the order"""
    reason_code: SheriffOrderReason | None = None
    """reason of the order"""
    reason_details: str | None = None
    """detailed explanation of reason of the order in user-readable form"""
    created_at: Timestamp
    """order creation timestamp - the real time when the order was created"""
    signature: bytes
    """the sheriff's signature (use ``SheriffOrder`` fingerprint)"""
    signature_version: int
    """signature version (i.e. fingerprint version)"""
    complaint_group_id: str | None = None
    """ID of the groups of complaints that were the cause of the order"""


class StoryAttributes(Structure):
    feed_name: str | None = None
    """name of the feed"""
    publish_at: Timestamp | None = None
    """story publication timestamp - the time the story must be published under in the feed"""
    pinned: bool | None = None
    """
    ``True``, if the story is pinned (should appear before any non-pinned story in the feed), ``False`` otherwise
    """
    viewed: bool | None = None
    """value of the ``viewed`` flag (``None``, if the flag is not changed)"""
    read: bool | None = None
    """value of the ``read`` flag (``None``, if the flag is not changed)"""
    satisfied: bool | None = None
    """value of the ``satisfied`` flag (``None``, if the flag is not changed)"""


class StorySummaryBlocked(Structure):
    operations: List[BlockedOperation]
    """list of the operations blocked"""
    period: int | None = None
    """the period of blocking in seconds"""


class StorySummaryFriendGroup(Structure):
    id: str | None = None
    """ID of the group of friends"""
    title: str | None = None
    """title of the group of friends"""


class StorySummaryEntry(Structure):
    owner_name: str | None = None
    """entry owner's name"""
    owner_full_name: str | None = None
    """entry owner's full name"""
    owner_gender: str | None = None
    """entry owner's gender"""
    heading: str | None = None
    """entry heading"""
    sheriffs: List[str] | None = None
    """list of sheriffs supervising the entry"""
    sheriff_marks: List[SheriffMark] | None = None
    """list of sheriff marks on the entry"""


class StorySummaryNode(Structure):
    owner_name: str | None = None
    """node owner's name"""
    owner_full_name: str | None = None
    """node owner's full name"""
    owner_gender: str | None = None
    """node owner's gender"""


class StorySummaryReaction(Structure):
    owner_name: str | None = None
    """reaction owner's name"""
    owner_full_name: str | None = None
    """reaction owner's full name"""
    owner_gender: str | None = None
    """reaction owner's gender"""
    emoji: int | None = None
    """reaction code"""


class StorySummarySheriff(Structure):
    sheriff_name: str
    """name of the sheriff"""
    order_id: str | None = None
    """ID of the sheriff's order"""
    complaint_id: str | None = None
    """ID of the complaint, if any"""


class SubscriberDescription(Structure):
    type: SubscriptionType
    """subscription type"""
    feed_name: str | None = None
    """feed name, if the subscription type requires one"""
    posting_id: str | None = None
    """posting ID, if the subscription type requires one"""
    last_updated_at: Timestamp | None = None
    """timestamp of the latest known state of the object"""
    operations: SubscriberOperations | None = None
    """the operations and the corresponding principals"""


class SubscriberInfo(Structure):
    id: str
    """subscriber ID"""
    type: SubscriptionType
    """subscription type"""
    feed_name: str | None = None
    """feed name, if the subscription type requires one"""
    posting_id: str | None = None
    """posting ID, if the subscription type requires one"""
    node_name: str
    """name of the subscribed node"""
    contact: ContactInfo | None = None
    """information known about the subscribed node"""
    created_at: Timestamp
    """subscription creation timestamp"""
    operations: SubscriberOperations | None = None
    """the supported operations and the corresponding principals"""
    owner_operations: SubscriberOperations | None = None
    """the supported operations and the corresponding principals as defined by the subscriber"""
    admin_operations: SubscriberOperations | None = None
    """the operations and the corresponding principals that are overridden by the node administrator"""


class SubscriberOverride(Structure):
    operations: SubscriberOperations | None = None
    """the supported operations and the corresponding principals"""
    admin_operations: SubscriberOperations | None = None
    """the operations and the corresponding principals that are overridden by the node administrator"""


class SubscriptionDescription(Structure):
    type: SubscriptionType
    """subscription type"""
    feed_name: str | None = None
    """the name of the feed on this node that receives notifications"""
    remote_node_name: str
    """the name of the node this node is subscribed to"""
    remote_feed_name: str | None = None
    """the name of the feed on the remote node, if the subscription type requires one"""
    remote_posting_id: str | None = None
    """posting ID on the remote node, if the subscription type requires one"""
    reason: SubscriptionReason | None = None
    """subscription reason"""
    operations: SubscriptionOperations | None = None
    """the operations and the corresponding principals"""


class SubscriptionFilter(Structure):
    type: SubscriptionType | None = None
    """subscription type"""
    feeds: List[RemoteFeed] | None = None
    """list of feeds"""
    postings: List[RemotePosting] | None = None
    """list of postings"""


class SubscriptionInfo(Structure):
    id: str
    """subscription ID"""
    type: SubscriptionType
    """subscription type"""
    feed_name: str | None = None
    """feed name on this node that receives notifications"""
    remote_node_name: str
    """name of the node this node is subscribed to"""
    contact: ContactInfo | None = None
    """information known about the remote node"""
    remote_feed_name: str | None = None
    """feed name on the remote node, if the subscription type requires one"""
    remote_posting_id: str | None = None
    """posting ID on the remote node, if the subscription type requires one"""
    created_at: Timestamp
    """subscription creation timestamp"""
    reason: SubscriptionReason
    """subscription reason"""
    operations: SubscriptionOperations | None = None
    """the supported operations and the corresponding principals"""


class SubscriptionOverride(Structure):
    operations: SubscriptionOperations | None = None
    """the supported operations and the corresponding principals"""


class TokenAttributes(Structure):
    login: str
    password: str
    auth_category: int | None = None
    """
    A bit mask describing which permissions should be granted to the token. If not set, all permissions of the
    administrator are granted. The bits have the following meaning:
    
    * ``other (0x0001)`` - any other permission not listed below;
    * ``view-media (0x0002)`` - view media files.
    """
    name: str | None = None
    """a user-readable name of the token"""


class TokenInfo(Structure):
    id: str
    """token ID (this is not the token, just an ID)"""
    token: str
    """the token"""
    name: str | None = None
    """a user-readable name of the token"""
    permissions: List[str] | None = None
    """
    The list of permissions granted to the token. The values are:
    
    * ``other`` - any other permission not listed below;
    * ``view-media`` - view media files.
    """
    plugin_name: str | None = None
    """a plugin the token belongs to; if set, only this plugin may use the token"""
    created_at: Timestamp
    """token creation timestamp"""
    deadline: Timestamp | None = None
    """timestamp of the end of the token's life"""
    last_used_at: Timestamp | None = None
    """timestamp of the last time the token was used"""
    last_used_browser: str | None = None
    """name of the browser used by the latest user of the token"""
    last_used_ip: str | None = None
    """IP address of the latest user of the token"""


class TokenName(Structure):
    name: str | None = None
    """a user-readable name of the token"""


class UpdateInfo(Structure):
    important: bool | None = None
    """``True``, if the update is important, ``False`` (the default) otherwise"""
    description: str | None = None
    """description of the update"""


class UserListInfo(Structure):
    name: str
    """name of the user list"""
    total: int
    """number of items in the user list"""


class UserListItemAttributes(Structure):
    node_name: str
    """the name of the node"""


class UserListItemInfo(Structure):
    node_name: str
    """the name of the node"""
    created_at: Timestamp
    """the node addition timestamp - the real time when the node was added to the list"""
    moment: int
    """moment of the node"""


class UserListSliceInfo(Structure):
    list_name: str
    """the name of the list"""
    before: int
    """the slice contains all items before this moment, inclusive. May be the far future."""
    after: int
    """the slice contains all items after this moment, exclusive. May be the far past."""
    items: List[UserListItemInfo]
    """the items"""
    total: int
    """total number of items"""
    total_in_past: int
    """number of items before this slice till the far past"""
    total_in_future: int
    """number of items after this slice till the far future"""


class WhoAmI(Structure):
    node_name: str | None = None
    node_name_changing: bool | None = None
    """``True`` if node name is about to be changed"""
    full_name: str | None = None
    """node owner's full name"""
    gender: str | None = None
    """node owner's gender"""
    title: str | None = None
    """node title"""
    avatar: AvatarImage | None = None
    """node owner's avatar"""
    frozen: bool | None = None
    """``True`` if the node is frozen due to inactivity, ``False`` (the default) otherwise"""


class ActivityReactionFilter(Structure):
    postings: List[RemotePosting] | None = None
    """include only reactions to remote postings from this list"""


class ActivityReactionInfo(Structure):
    remote_node_name: str
    """name of the remote node"""
    remote_full_name: str | None = None
    """full name of the remote node"""
    remote_avatar: AvatarImage | None = None
    """avatar of the remote node"""
    remote_posting_id: str
    """ID of the posting on the remote node"""
    negative: bool
    """``True``, if the reaction is negative, ``False``, if positive"""
    emoji: int
    """reaction code, usually interpreted by clients as emoji code point"""
    created_at: Timestamp
    """reaction creation timestamp - the real time when the reaction was created"""


class BlockedByUserFilter(Structure):
    blocked_operations: List[BlockedOperation] | None = None
    """operations that are blocked"""
    postings: List[RemotePostingOrNode] | None = None
    """the postings or whole nodes, where the node is blocked"""
    strict: bool | None = None
    """
    if set to ``True``, only the blockings that strictly fit the criteria are returned; otherwise global blockings are
    returned even if the search is limited to a particular posting
    """


class BlockedByUserInfo(Structure):
    id: str
    blocked_operation: BlockedOperation
    """operation that is blocked"""
    contact: ContactInfo | None = None
    """information known about the blocking node"""
    node_name: str
    """name of the blocking node"""
    posting_id: str | None = None
    """ID of the posting, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    created_at: Timestamp
    """blocking timestamp - the real time when the node was blocked"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the node will be unblocked; ``None`` or absent, if the node is blocked
    permanently
    """
    reason: str | None = None
    """reason of blocking"""


class BlockedUserInfo(Structure):
    id: str
    blocked_operation: BlockedOperation
    """operation that is blocked"""
    node_name: str
    """name of the blocked node"""
    contact: ContactInfo | None = None
    """information known about the blocked node"""
    entry_id: str | None = None
    """ID of the local entry, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    entry_node_name: str | None = None
    """
    node name of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally
    """
    entry_posting_id: str | None = None
    """ID of the remote posting, where the node is blocked; ``None`` or absent, if the node is blocked globally"""
    created_at: Timestamp
    """blocking timestamp - the real time when the node was blocked"""
    deadline: Timestamp | None = None
    """
    unblocking timestamp - the real time when the node will be unblocked; ``None`` or absent, if the node is blocked
    permanently
    """
    reason_src: str | None = None
    """source text of the reason of blocking"""
    reason_src_format: SourceFormat | None = None
    """
    format of the source text of the reason of blocking, the list of available formats is returned in
    ``PostingFeatures``
    """
    reason: str | None = None
    """reason of blocking"""


class Body(Structure):
    subject: str | None = None
    """the subject (plain text)"""
    text: str | None = None
    """the text (HTML)"""
    link_previews: List[LinkPreview] | None = None
    """link previews"""


class CommentRevisionInfo(Structure):
    id: str
    posting_revision_id: str
    """ID of the posting revision that was actual at the moment of creation of this comment revision"""
    body_preview: Body | None = None
    """preview of the revision's body, a string representation of a JSON structure"""
    body_src_hash: bytes
    """hash of the source text of the revision"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the revision, the list of available formats is returned in ``PostingFeatures``
    """
    body: Body
    """body of the revision, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the revision, may have any value meaningful for the client"""
    heading: str
    """heading of the revision"""
    created_at: Timestamp
    """revision creation timestamp - the real time when the revision was created"""
    deleted_at: Timestamp | None = None
    """revision deletion timestamp - the time when the revision was deleted"""
    deadline: Timestamp | None = None
    """
    revision deletion timestamp - the time when the revision will be deleted and the previous revision will take its
    place
    """
    digest: bytes | None = None
    """cryptographic digest of the revision (use ``Comment`` fingerprint)"""
    signature: bytes | None = None
    """the comment's owner signature (use ``Comment`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    client_reaction: ClientReactionInfo | None = None
    """details of the existing reaction (if any) of the client's owner"""
    reactions: ReactionTotalsInfo | None = None
    """summary of reactions to the revision"""


class CommentSourceText(Structure):
    owner_avatar: AvatarDescription | None = None
    """avatar of the comment's owner"""
    body_src: Body | None = None
    """the source text of the comment, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the comment, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    media: List[MediaWithDigest] | None = None
    """array of IDs and digests of private media to be attached to the comment"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the comment accepts"""
    replied_to_id: str | None = None
    """ID of the comment this comment is replying to"""
    operations: CommentOperations | None = None
    """the operations and the corresponding principals"""
    senior_operations: CommentOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the posting's owner ("senior"); only the
    senior may set this
    """


class CommentText(Structure):
    owner_name: str | None = None
    """node name of the comment's owner"""
    owner_full_name: str | None = None
    """full name of the comment's owner"""
    owner_gender: str | None = None
    """gender of the comment's owner"""
    owner_avatar: AvatarDescription | None = None
    """avatar of the comment's owner"""
    body_preview: Body | None = None
    """preview of the comment's body, a string representation of a JSON structure"""
    body_src: Body | None = None
    """the source text of the comment, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the comment, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    body: Body | None = None
    """body of the comment, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the comment, may have any value meaningful for the client"""
    media: List[str] | None = None
    """array of IDs of private media to be attached to the comment"""
    created_at: Timestamp | None = None
    """comment creation timestamp - the real time when the comment was created"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the comment accepts"""
    replied_to_id: str | None = None
    """ID of the comment this comment is replying to"""
    signature: bytes | None = None
    """the comment's owner signature (use ``Comment`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    operations: CommentOperations | None = None
    """the operations and the corresponding principals"""
    reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the comment"""
    senior_operations: CommentOperations | None = None
    """
    the operations and the corresponding principals that are overridden by the posting's owner ("senior"); only the
    senior may set this
    """


class DraftText(Structure):
    draft_type: DraftType
    """type of the draft"""
    receiver_name: str
    """name of the node the draft is related to"""
    receiver_posting_id: str | None = None
    """ID of the posting, mandatory for all types, except ``new-posting``"""
    receiver_comment_id: str | None = None
    """ID of the comment, mandatory for ``comment-update`` type"""
    replied_to_id: str | None = None
    """ID of the comment replied to"""
    owner_full_name: str | None = None
    """full name of the posting's/comment's owner"""
    owner_avatar: AvatarDescription | None = None
    """avatar of the posting's/comment's owner"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the posting accepts"""
    body_src: Body | None = None
    """the source text of the draft, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the draft, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    media: List[RemoteMedia] | None = None
    """list of the media attached to the draft, the media may be located on another node"""
    publish_at: int | None = None
    """story publication timestamp - the time the story must be published under in the feed"""
    update_info: UpdateInfo | None = None
    """description of the update"""
    operations: PostingOperations | None = None
    """draft of the list of operations and the corresponding principals"""
    comment_operations: CommentOperations | None = None
    """
    draft of the list of operations and the corresponding principals that are overridden in the posting's comments
    """


class Features(Structure):
    posting: PostingFeatures
    """features of a posting"""
    plugins: List[str] | None = None
    """list of names of plugins enabled for the node"""
    feed_width: int
    """width of the feed in pixels"""
    friend_groups: FriendGroupsFeatures | None = None
    """features of groups of friends"""
    ask: List[AskSubject] | None = None
    """list of requests to the node owner that are accepted by the node"""
    subscribed: bool | None = None
    """``True``, if the node is subscribed to the client, ``False`` otherwise"""


class FeedInfo(Structure):
    feed_name: str
    """name of the feed"""
    title: str | None = None
    """title of the feed"""
    total: int
    """total number of stories in the feed"""
    first_created_at: Timestamp | None = None
    """creation timestamp of the earliest story in the feed"""
    last_created_at: Timestamp | None = None
    """creation timestamp of the latest story in the feed"""
    operations: FeedOperations | None = None
    """the supported operations and the corresponding principals"""
    sheriffs: List[str] | None = None
    """list of sheriffs supervising the feed"""
    sheriff_marks: List[SheriffMark] | None = None
    """list of sheriff marks on the feed"""


class FriendDescription(Structure):
    node_name: str
    """name of the node"""
    groups: List[FriendGroupAssignment] | None = None
    """groups of friends the node is to be included into"""


class MediaAttachment(Structure):
    media: PrivateMediaFileInfo | None = None
    """details of the attached media, may be absent if the media is not located on the node"""
    remote_media: RemoteMediaInfo | None = None
    """details of the media, if it is located on another node"""
    embedded: bool
    """``True`` if the media is used in the body of the posting/comment, ``False`` otherwise"""


class PostingInfo(Structure):
    id: str
    revision_id: str
    """ID of the current revision of the posting"""
    receiver_revision_id: str | None = None
    """ID of the current revision of the original posting (for cached copies of remote postings only)"""
    total_revisions: int
    """total number of revisions the posting has"""
    receiver_name: str | None = None
    """name of the node where the posting was published (for cached copies of remote postings only)"""
    receiver_full_name: str | None = None
    """full name of the node where the posting was published (for cached copies of remote postings only)"""
    receiver_gender: str | None = None
    """gender of the node where the posting was published (for cached copies of remote postings only)"""
    receiver_avatar: AvatarImage | None = None
    """avatar of the node where the posting was published (for cached copies of remote postings only)"""
    receiver_posting_id: str | None = None
    """ID of the original posting (for cached copies of remote postings only)"""
    parent_media_id: str | None = None
    """ID of the media the posting is linked to, if any"""
    owner_name: str
    """node name of the posting's owner"""
    owner_full_name: str | None = None
    """full name of the posting's owner"""
    owner_gender: str | None = None
    """gender of the posting's owner"""
    owner_avatar: AvatarImage | None = None
    """avatar of the posting's owner"""
    body_preview: Body | None = None
    """preview of the posting's body, a string representation of a JSON structure"""
    body_src: Body | None = None
    """
    the source text of the posting, a string representation of a JSON structure, may be absent if not requested
    """
    body_src_hash: bytes
    """hash of the source text of the posting"""
    body_src_format: SourceFormat | None = None
    """format of the source text of the posting, the list of available formats is returned in ``PostingFeatures``"""
    body: Body
    """body of the posting, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the posting, may have any value meaningful for the client"""
    media: List[MediaAttachment] | None = None
    """list of the media attached to the posting"""
    heading: str
    """heading of the posting"""
    update_info: UpdateInfo | None = None
    """description of the latest update"""
    created_at: Timestamp
    """posting creation timestamp - the real time when the posting was created"""
    edited_at: Timestamp | None = None
    """posting editing timestamp - the last time the posting was updated"""
    deleted_at: Timestamp | None = None
    """posting deletion timestamp - the time when the posting was deleted"""
    receiver_created_at: Timestamp | None = None
    """original posting creation timestamp (for cached copies of remote postings only)"""
    receiver_edited_at: Timestamp | None = None
    """original posting editing timestamp (for cached copies of remote postings only)"""
    receiver_deleted_at: Timestamp | None = None
    """original posting deletion timestamp (for cached copies of remote postings only)"""
    revision_created_at: Timestamp
    """creation timestamp of the current revision of the posting"""
    receiver_revision_created_at: Timestamp | None = None
    """
    creation timestamp of the current revision of the original posting (for cached copies of remote postings only)
    """
    deadline: Timestamp | None = None
    """posting purging timestamp - the time when the deleted posting will be purged from the database"""
    digest: bytes | None = None
    """cryptographic digest of the posting (use ``Posting`` fingerprint)"""
    signature: bytes | None = None
    """the posting's owner signature (use ``Posting`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    feed_references: List[FeedReference] | None = None
    """array of references to the posting from stories in feeds"""
    blocked_instants: List[BlockedPostingInstantInfo] | None = None
    """instants related to the posting that are blocked (for admin only)"""
    operations: PostingOperations | None = None
    """the supported operations and the corresponding principals"""
    receiver_operations: PostingOperations | None = None
    """
    the supported operations for the original posting and the corresponding principals (for cached copies of remote
    postings only)
    """
    comment_operations: CommentOperations | None = None
    """the operations and the corresponding principals that are overridden in the posting's comments"""
    reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the posting"""
    comment_reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the posting's comments"""
    blocked_operations: List[BlockedEntryOperation] | None = None
    """operations on the posting that are blocked for the client"""
    blocked_comment_operations: List[BlockedEntryOperation] | None = None
    """operations on the posting's comments that are blocked for the client"""
    sheriffs: List[str] | None = None
    """list of sheriffs supervising the posting"""
    sheriff_marks: List[SheriffMark] | None = None
    """list of sheriff marks on the posting"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the posting accepts"""
    client_reaction: ClientReactionInfo | None = None
    """details of the existing reaction (if any) of the client's owner"""
    reactions: ReactionTotalsInfo | None = None
    """reactions summary of the posting"""
    sources: List[PostingSourceInfo] | None = None
    """details of the sources the posting was received from (for cached copies of remote postings only)"""
    total_comments: int | None = None
    """total number of comments to the posting"""


class PostingRevisionInfo(Structure):
    id: str
    receiver_id: str | None = None
    """ID of the original revision (for cached copies of remote postings only)"""
    body_preview: Body | None = None
    """preview of the revision's body, a string representation of a JSON structure"""
    body_src_hash: bytes
    """hash of the source text of the revision"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the revision, the list of available formats is returned in ``PostingFeatures``
    """
    body: Body
    """body of the revision, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the revision"""
    media: List[MediaAttachment] | None = None
    """list of the media attached to the revision"""
    heading: str
    """heading of the revision"""
    update_info: UpdateInfo | None = None
    """description of the latest update"""
    created_at: Timestamp
    """revision creation timestamp - the real time when the revision was created"""
    deleted_at: Timestamp | None = None
    """revision deletion timestamp - the time when the revision was deleted"""
    receiver_created_at: Timestamp | None = None
    """original revision creation timestamp (for cached copies of remote postings only)"""
    receiver_deleted_at: Timestamp | None = None
    """original revision deletion timestamp (for cached copies of remote postings only)"""
    digest: bytes | None = None
    """cryptographic digest of the revision (use ``Posting`` fingerprint)"""
    signature: bytes | None = None
    """the revision's owner signature (use ``Posting`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    client_reaction: ClientReactionInfo | None = None
    """details of the existing reaction (if any) of the client's owner"""
    reactions: ReactionTotalsInfo | None = None
    """reactions summary of the posting revision"""


class PostingSourceText(Structure):
    owner_avatar: AvatarDescription | None = None
    """avatar of the posting's owner"""
    body_src: Body | None = None
    """the source text of the posting, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the posting, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    media: List[MediaWithDigest] | None = None
    """array of IDs and digests of private media to be attached to the posting"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the posting accepts"""
    operations: PostingOperations | None = None
    """the operations and the corresponding principals"""
    comment_operations: CommentOperations | None = None
    """the operations and the corresponding principals that are overridden in the posting's comments"""


class PostingText(Structure):
    owner_name: str | None = None
    """node name of the posting's owner"""
    owner_full_name: str | None = None
    """full name of the posting's owner"""
    owner_gender: str | None = None
    """gender of the posting's owner"""
    owner_avatar: AvatarDescription | None = None
    """avatar of the posting's owner"""
    body_preview: Body | None = None
    """preview of the posting's body, a string representation of a JSON structure"""
    body_src: Body | None = None
    """the source text of the posting, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the posting, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    body: Body | None = None
    """body of the posting, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the posting, may have any value meaningful for the client"""
    media: List[str] | None = None
    """array of IDs of private media to be attached to the posting"""
    created_at: Timestamp | None = None
    """posting creation timestamp - the real time when the posting was created"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the posting accepts"""
    publications: List[StoryAttributes] | None = None
    """list of publications in feeds that must be made after creating the posting (for new postings only)"""
    update_info: UpdateInfo | None = None
    """description of the update"""
    signature: bytes | None = None
    """the posting's owner signature (use ``Posting`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    operations: PostingOperations | None = None
    """the operations and the corresponding principals"""
    comment_operations: CommentOperations | None = None
    """the operations and the corresponding principals that are overridden in the posting's comments"""
    reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the posting"""
    comment_reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the posting's comments"""


class ReactionCreated(Structure):
    reaction: ReactionInfo | None = None
    """details of the reaction created"""
    totals: ReactionTotalsInfo
    """summary of reactions after the creation"""


class SettingDescriptor(Structure):
    name: str
    """name of the setting"""
    type: SettingType
    """type of the setting"""
    default_value: str | None = None
    """default value of the setting"""
    internal: bool | None = None
    """the setting is internal - not displayed to the user"""
    privileged: bool | None = None
    """the setting is privileged - may be changed by server owner only"""
    title: str | None = None
    """human-friendly description of the setting"""
    modifiers: SettingTypeModifiers | None = None
    """
    additional modifiers that may help to choose a proper UI component for the setting value and to validate the input;
    the meaning of the modifiers depends on the setting type
    """


class SettingMetaInfo(Structure):
    name: str
    """name of the setting"""
    type: SettingType
    """type of the setting"""
    default_value: str | None = None
    """default value of the setting"""
    privileged: bool | None = None
    """the setting is privileged - may be changed by server owner only"""
    title: str
    """human-friendly description of the setting"""
    modifiers: SettingTypeModifiers | None = None
    """
    additional modifiers that may help to choose a proper UI component for the setting value and to validate the input;
    the meaning of the modifiers depends on the setting type
    """


class StorySummaryData(Structure):
    node: StorySummaryNode | None = None
    """a node"""
    posting: StorySummaryEntry | None = None
    """a posting"""
    comment: StorySummaryEntry | None = None
    """a comment"""
    comments: List[StorySummaryEntry] | None = None
    """list of comments"""
    total_comments: int | None = None
    """total number of comments"""
    replied_to: StorySummaryEntry | None = None
    """the comment replied to"""
    parent_posting: StorySummaryEntry | None = None
    """the parent posting of the media"""
    reaction: StorySummaryReaction | None = None
    """a reaction"""
    reactions: List[StorySummaryReaction] | None = None
    """list of reactions"""
    total_reactions: int | None = None
    """total number of reactions"""
    feed_name: str | None = None
    """name of a feed"""
    subscription_reason: SubscriptionReason | None = None
    """subscription reason"""
    friend_group: StorySummaryFriendGroup | None = None
    """a group of friends"""
    blocked: StorySummaryBlocked | None = None
    """summary of blocking a user"""
    sheriff: StorySummarySheriff | None = None
    """summary of an action of a sheriff"""
    description: str | None = None
    """additional descriptive text"""


class CommentInfo(Structure):
    id: str
    owner_name: str
    """node name of the comment's owner"""
    owner_full_name: str | None = None
    """full name of the comment's owner"""
    owner_gender: str | None = None
    """gender of the comment's owner"""
    owner_avatar: AvatarImage | None = None
    """avatar of the comment's owner"""
    posting_id: str
    """ID of the parent posting of the comment"""
    posting_revision_id: str
    """ID of the revision of parent posting that was current when the comment was created"""
    revision_id: str
    """ID of the current revision of the comment"""
    total_revisions: int
    """total number of revisions the comment has"""
    body_preview: Body | None = None
    """preview of the comment's body, a string representation of a JSON structure"""
    body_src: Body | None = None
    """
    the source text of the comment, a string representation of a JSON structure, may be absent if not requested
    """
    body_src_hash: bytes
    """hash of the source text of the comment"""
    body_src_format: SourceFormat | None = None
    """format of the source text of the comment, the list of available formats is returned in ``PostingFeatures``"""
    body: Body
    """body of the comment, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the comment, may have any value meaningful for the client"""
    media: List[MediaAttachment] | None = None
    """list of the media attached to the comment"""
    heading: str
    """heading of the comment"""
    replied_to: RepliedTo | None = None
    """information about the comment this comment is replying to"""
    moment: int
    created_at: Timestamp
    """comment creation timestamp - the real time when the comment was created"""
    edited_at: Timestamp | None = None
    """comment editing timestamp - the last time the comment was updated"""
    deleted_at: Timestamp | None = None
    """comment deletion timestamp - the time when the comment was deleted"""
    revision_created_at: Timestamp
    """creation timestamp of the current revision of the comment"""
    deadline: Timestamp | None = None
    """comment purging timestamp - the time when the deleted comment will be purged from the database"""
    digest: bytes | None = None
    """cryptographic digest of the comment (use ``Comment`` fingerprint)"""
    signature: bytes | None = None
    """the comment's owner signature (use ``Comment`` fingerprint)"""
    signature_version: int | None = None
    """signature version (i.e. fingerprint version)"""
    operations: CommentOperations | None = None
    """the supported operations and the corresponding principals"""
    reaction_operations: ReactionOperations | None = None
    """the operations and the corresponding principals that are overridden in reactions to the comment"""
    owner_operations: CommentOperations | None = None
    """the supported operations and the corresponding principals as defined by the comment's owner"""
    senior_operations: CommentOperations | None = None
    """the operations and the corresponding principals that are overridden by the posting's owner ("senior")"""
    blocked_operations: List[BlockedEntryOperation] | None = None
    """operations on the comment that are blocked for the client"""
    sheriff_marks: List[SheriffMark] | None = None
    """list of sheriff marks on the comment"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the comment accepts"""
    client_reaction: ClientReactionInfo | None = None
    """details of the existing reaction (if any) of the client's owner"""
    senior_reaction: ClientReactionInfo | None = None
    """details of the existing reaction (if any) of the posting's owner ("senior") to the comment"""
    reactions: ReactionTotalsInfo | None = None
    """summary of reactions to the comment"""


class CommentsSliceInfo(Structure):
    before: int
    """the slice contains all comments before this moment, inclusive. May be the far future."""
    after: int
    """the slice contains all comments after this moment, exclusive. May be the far past."""
    comments: List[CommentInfo]
    """the comments"""
    total: int
    """total number of comments"""
    total_in_past: int
    """number of comments before this slice till the far past"""
    total_in_future: int
    """number of comments after this slice till the far future"""


class DraftInfo(Structure):
    id: str
    draft_type: DraftType
    """type of the draft"""
    receiver_name: str
    """name of the node the draft is related to"""
    receiver_posting_id: str | None = None
    """ID of the posting, set for all types, except ``new-posting``"""
    receiver_comment_id: str | None = None
    """ID of the comment, set for ``comment-update`` type"""
    replied_to_id: str | None = None
    """ID of the comment replied to, set for comment drafts, if needed"""
    created_at: Timestamp
    """draft creation timestamp - the real time when the draft was created"""
    edited_at: Timestamp | None = None
    """draft editing timestamp - the last time the draft was updated"""
    deadline: Timestamp | None = None
    """draft purging timestamp - the time when the draft will be purged from the database, if not updated"""
    owner_full_name: str | None = None
    """full name of the posting's/comment's owner"""
    owner_avatar: AvatarImage | None = None
    """avatar of the posting's/comment's owner"""
    accepted_reactions: AcceptedReactions | None = None
    """types of reactions that the posting accepts"""
    body_src: Body | None = None
    """the source text of the draft, a string representation of a JSON structure"""
    body_src_format: SourceFormat | None = None
    """
    format of the source text of the draft, ``plain-text`` by default; the list of available formats is returned in
    ``PostingFeatures``
    """
    body: Body
    """body of the draft, a string representation of a JSON structure"""
    body_format: BodyFormat | None = None
    """format of the body of the draft"""
    media: List[MediaAttachment] | None = None
    """list of the media attached to the draft"""
    heading: str
    """heading of the draft"""
    publish_at: int | None = None
    """story publication timestamp - the time the story must be published under in the feed"""
    update_info: UpdateInfo | None = None
    """description of the update"""
    operations: PostingOperations | None = None
    """draft of the list of operations and the corresponding principals"""
    comment_operations: CommentOperations | None = None
    """
    draft of the list of operations and the corresponding principals that are overridden in the posting's comments, set
    for posting drafts, if needed
    """


class EntryInfo(Structure):
    posting: PostingInfo | None = None
    """posting details, set if the entry is a posting"""
    comment: CommentInfo | None = None
    """comment details, set if the entry is a comment"""


class PluginDescription(Structure):
    name: str
    """a unique plugin name; can contain only small latin letters, digits or hyphen"""
    title: str | None = None
    """user-readable title of the plugin"""
    description: str | None = None
    """user-readable description of the purpose of the plugin"""
    location: str | None = None
    """URL of the plugin; used by the node to call the plugin API"""
    accepted_events: List[str] | None = None
    """list of types of internal events the plugin wants to receive; Read more about internal events."""
    options: List[SettingDescriptor] | None = None
    """
    plugin settings to be added to the list of node settings, the settings appear in the list with a prefix
    ``plugin.&lt;plugin name>.``
    """


class PluginInfo(Structure):
    node_id: str
    """ID of the node this plugin is connected to"""
    local: bool
    """
    ``True`` if the plugin is enabled for a particular node only, ``False``, if it is enabled for the whole server
    """
    name: str
    """a unique plugin name"""
    title: str | None = None
    """user-readable title of the plugin"""
    description: str | None = None
    """user-readable description of the purpose of the plugin"""
    location: str | None = None
    """URL of the plugin; used by the node to call the plugin API"""
    accepted_events: List[str] | None = None
    """list of types of internal events the plugin wants to receive; Read more about internal events."""
    settings: List[SettingMetaInfo] | None = None
    """plugin settings to be added to the list of node settings"""
    token_id: str | None = None
    """ID of the token used to authenticate the plugin"""


class StoryInfo(Structure):
    id: str
    feed_name: str
    """name of the feed"""
    story_type: StoryType
    """type of the story"""
    created_at: Timestamp
    """story creation timestamp - the real time when the story was created"""
    published_at: Timestamp
    """story publication timestamp - the time the story is published under in the feed"""
    pinned: bool | None = None
    """
    ``True``, if the story is pinned (should appear before any non-pinned story in the feed), ``False`` otherwise
    """
    moment: int
    viewed: bool | None = None
    """``True``, if the story has been viewed by node owner, ``False`` otherwise"""
    read: bool | None = None
    """``True``, if the story has been read by node owner, ``False`` otherwise"""
    satisfied: bool | None = None
    """
    if the story is associated with a user action (for example, it contains a form that should be submitted), this flag
    is set to ``True`` if the action is done already, and ``False`` otherwise
    """
    summary_node_name: str | None = None
    """name of the node related to the summary of the story"""
    summary_full_name: str | None = None
    """full name of the node related to the summary of the story"""
    summary_avatar: AvatarImage | None = None
    """avatar of the summary of the story"""
    summary: str | None = None
    """user-readable summary of the story - this field is **deprecated** in favor of ``summaryData``"""
    summary_data: StorySummaryData | None = None
    """details of the story; they are used by the client to build a user-readable summary of the story"""
    posting: PostingInfo | None = None
    """the posting this story is about"""
    posting_id: str | None = None
    """ID of the posting this story is about, used if the whole posting is not returned"""
    comment: CommentInfo | None = None
    """the comment this story is about"""
    comment_id: str | None = None
    """ID of the comment this story is about, used if the whole posting is not returned"""
    remote_node_name: str | None = None
    """name of the node this story is about"""
    remote_full_name: str | None = None
    """full name of the node this story is about"""
    remote_posting_id: str | None = None
    """ID of the posting at remote node this story is about"""
    remote_comment_id: str | None = None
    """ID of the comment at remote node this story is about"""
    remote_media_id: str | None = None
    """ID of the media at remote node this story is about"""
    operations: StoryOperations | None = None
    """the supported operations and the corresponding principals"""


class CommentCreated(Structure):
    comment: CommentInfo
    """details of the comment created"""
    total: int
    """total number of comments in the posting after the creation"""


class FeedSliceInfo(Structure):
    before: int
    """the slice contains all stories before this moment, inclusive. May be the far future."""
    after: int
    """the slice contains all stories after this moment, exclusive. May be the far past."""
    stories: List[StoryInfo]
    """the stories"""
    total_in_past: int
    """total number of stories in the feed before this slice"""
    total_in_future: int
    """total number of stories in the feed after this slice"""


class PushContent(Structure):
    type: PushContentType
    """type of the notification"""
    id: str | None = None
    """ID of the story (``story-deleted`` notifications only)"""
    story: StoryInfo | None = None
    """the story (``story-added`` notifications only)"""
    feed_status: FeedWithStatus | None = None
    """status of the feed (``feed-updated`` notifications only)"""
