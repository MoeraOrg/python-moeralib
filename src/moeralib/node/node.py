# This file is generated

from typing import IO, List, cast
from urllib.parse import quote_plus

from . import types, schemas
from .caller import Caller
from ..structure import comma_separated_flags, structure_list


class MoeraNode(Caller):
    """Node API interface."""

    def __init__(self, node_url: str | None = None):
        if node_url is not None:
            self.node_url(node_url)

    def search_activity_reactions(self, filter: types.ActivityReactionFilter) -> List[types.ActivityReactionInfo]:
        """
        Get the list of all reactions performed by the node, filtered by some criteria.

        :param filter:
        """
        location = "/activity/reactions/search"
        data = self.call(
            "search_activity_reactions", location, method="POST", body=filter,
            schema=schemas.ACTIVITY_REACTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ActivityReactionInfo)

    def get_remote_posting_verification_status(self, id: str) -> types.RemotePostingVerificationInfo:
        """
        Get the status of the asynchronous operation that performs verification of a remote posting signature.

        :param id: asynchronous operation ID
        """
        location = "/async-operations/remote-posting-verification/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_remote_posting_verification_status", location, method="GET",
            schema=schemas.REMOTE_POSTING_VERIFICATION_INFO_SCHEMA
        )
        return types.RemotePostingVerificationInfo.from_json(data)

    def get_remote_reaction_verification_status(self, id: str) -> types.RemoteReactionVerificationInfo:
        """
        Get the status of the asynchronous operation that performs verification of the signature of a reaction to a
        remote posting.

        :param id: asynchronous operation ID
        """
        location = "/async-operations/remote-reaction-verification/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_remote_reaction_verification_status", location, method="GET",
            schema=schemas.REMOTE_REACTION_VERIFICATION_INFO_SCHEMA
        )
        return types.RemoteReactionVerificationInfo.from_json(data)

    def get_avatars(self) -> List[types.AvatarInfo]:
        """
        Get the list of avatars in the ascending order of their ordinals.
        """
        location = "/avatars"
        data = self.call("get_avatars", location, method="GET", auth=False, schema=schemas.AVATAR_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.AvatarInfo)

    def create_avatar(self, avatar: types.AvatarAttributes) -> types.AvatarInfo:
        """
        Create a new avatar from a public media file that exists on the node. A new public media file is created for
        the avatar. If the avatar's ordinal is not provided in the input, the avatar is assigned an ordinal that is
        greater than ordinals of all existing avatars.

        :param avatar:
        """
        location = "/avatars"
        data = self.call("create_avatar", location, method="POST", body=avatar, schema=schemas.AVATAR_INFO_SCHEMA)
        return types.AvatarInfo.from_json(data)

    def get_avatar(self, id: str) -> types.AvatarInfo:
        """
        Get an individual avatar.

        :param id: avatar ID
        """
        location = "/avatars/{id}".format(id=quote_plus(id))
        data = self.call("get_avatar", location, method="GET", auth=False, schema=schemas.AVATAR_INFO_SCHEMA)
        return types.AvatarInfo.from_json(data)

    def delete_avatar(self, id: str) -> types.Result:
        """
        Delete an avatar.

        :param id: avatar ID
        """
        location = "/avatars/{id}".format(id=quote_plus(id))
        data = self.call("delete_avatar", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def reorder_avatars(self, order: types.AvatarsOrdered) -> List[types.AvatarOrdinal]:
        """
        Reorder avatars. Every avatar mentioned in the input is assigned an ordinal in ascending order as they appear
        in the input. Ordinals of avatars not mentioned in the input are not touched.

        :param order:
        """
        location = "/avatars/reorder"
        data = self.call(
            "reorder_avatars", location, method="POST", body=order, schema=schemas.AVATAR_ORDINAL_ARRAY_SCHEMA
        )
        return structure_list(data, types.AvatarOrdinal)

    def block_instant(self, instant: types.BlockedInstantAttributes) -> types.BlockedInstantInfo:
        """
        Blocks creation of instants of the given story type, related to the given entry, optionally unblocking at the
        given time in the future.

        :param instant:
        """
        location = "/blocked-instants"
        data = self.call(
            "block_instant", location, method="POST", body=instant, schema=schemas.BLOCKED_INSTANT_INFO_SCHEMA
        )
        return types.BlockedInstantInfo.from_json(data)

    def get_blocked_instant(self, id: str) -> types.BlockedInstantInfo:
        """
        Get details about the given blocked instant.

        :param id: ID of the blocked instant
        """
        location = "/blocked-instants/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_instant", location, method="GET", schema=schemas.BLOCKED_INSTANT_INFO_SCHEMA)
        return types.BlockedInstantInfo.from_json(data)

    def unblock_instant(self, id: str) -> types.Result:
        """
        Unblock the given instant.

        :param id: ID of the blocked instant
        """
        location = "/blocked-instants/{id}".format(id=quote_plus(id))
        data = self.call("unblock_instant", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def search_blocked_instants(self, filter: types.BlockedInstantFilter) -> List[types.BlockedInstantInfo]:
        """
        Search blocked instants by the given criteria.

        :param filter:
        """
        location = "/blocked-instants/search"
        data = self.call(
            "search_blocked_instants", location, method="POST", body=filter,
            schema=schemas.BLOCKED_INSTANT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedInstantInfo)

    def block_user(self, user: types.BlockedUserAttributes) -> types.BlockedUserInfo:
        """
        Blocks the given node from performing the given operations, in a particular posting or globally, optionally
        unblocking at the given time in the future.

        :param user:
        """
        location = "/people/blocked-users"
        data = self.call("block_user", location, method="POST", body=user, schema=schemas.BLOCKED_USER_INFO_SCHEMA)
        return types.BlockedUserInfo.from_json(data)

    def get_blocked_user(self, id: str) -> types.BlockedUserInfo:
        """
        Get details about the given blocked user.

        :param id: ID of the blocked user
        """
        location = "/people/blocked-users/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_user", location, method="GET", schema=schemas.BLOCKED_USER_INFO_SCHEMA)
        return types.BlockedUserInfo.from_json(data)

    def unblock_user(self, id: str) -> types.Result:
        """
        Unblock the given user.

        :param id: ID of the blocked user
        """
        location = "/people/blocked-users/{id}".format(id=quote_plus(id))
        data = self.call("unblock_user", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def search_blocked_users(self, filter: types.BlockedUserFilter) -> List[types.BlockedUserInfo]:
        """
        Search blocked users by the given criteria.

        :param filter:
        """
        location = "/people/blocked-users/search"
        data = self.call(
            "search_blocked_users", location, method="POST", body=filter, schema=schemas.BLOCKED_USER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedUserInfo)

    def get_blocked_users_checksums(self) -> types.BlockedUsersChecksums:
        """
        Get checksums of the information about the blocked users. This request may be used to quickly detect the
        changes in the blocked users list to update the cache on the client side.
        """
        location = "/people/blocked-users/checksums"
        data = self.call(
            "get_blocked_users_checksums", location, method="GET", schema=schemas.BLOCKED_USERS_CHECKSUMS_SCHEMA
        )
        return types.BlockedUsersChecksums.from_json(data)

    def get_blocked_by_user(self, id: str) -> types.BlockedByUserInfo:
        """
        Get details about the given node that blocked this node.

        :param id: ID of the blocked-by user
        """
        location = "/people/blocked-by-users/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_by_user", location, method="GET", schema=schemas.BLOCKED_BY_USER_INFO_SCHEMA)
        return types.BlockedByUserInfo.from_json(data)

    def search_blocked_by_users(self, filter: types.BlockedByUserFilter) -> List[types.BlockedByUserInfo]:
        """
        Search nodes that blocked this node, by the given criteria.

        :param filter:
        """
        location = "/people/blocked-by-users/search"
        data = self.call(
            "search_blocked_by_users", location, method="POST", body=filter,
            schema=schemas.BLOCKED_BY_USER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedByUserInfo)

    def get_cartes(self, limit: int | None = None) -> types.CarteSet:
        """
        Get a set of cartes that correspond to successive periods of time. Two sequences of cartes are returned: one
        with all permissions and another with `view-media` permission only. The node may decide to return fewer cartes
        than the given ``limit``.

        :param limit: maximum number of sequential cartes returned
        """
        location = "/cartes".format()
        params = {"limit": limit}
        data = self.call("get_cartes", location, method="GET", params=params, schema=schemas.CARTE_SET_SCHEMA)
        return types.CarteSet.from_json(data)

    def get_comments_slice(
        self, posting_id: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.CommentsSliceInfo:
        """
        Get a slice of the list of comments, delimited by ``before`` or ``after`` moments (but not both) and the given
        ``limit``. If neither ``before`` nor ``after`` are provided, the latest comments are returned. The node may
        decide to return fewer comments than the given ``limit``. The stories are always sorted by moment, ascending.

        :param posting_id: ID of the posting
        :param after: filter comments posted strongly after this moment
        :param before: filter comments posted at or before this moment
        :param limit: maximum number of comments returned
        """
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_comments_slice", location, method="GET", params=params, bodies=True,
            schema=schemas.COMMENTS_SLICE_INFO_SCHEMA
        )
        return types.CommentsSliceInfo.from_json(data)

    def create_comment(self, posting_id: str, comment: types.CommentText) -> types.CommentCreated:
        """
        Create a comment from the given text and add it to the given posting. The comment owner must authenticate in
        some way. If the comment is not signed, it will be kept for a limited period of time and then erased. If
        authenticated as admin, the node signs the comment.

        :param posting_id: ID of the posting
        :param comment:
        """
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        data = self.call(
            "create_comment", location, method="POST", src_bodies=True, body=comment, bodies=True,
            schema=schemas.COMMENT_CREATED_SCHEMA
        )
        return types.CommentCreated.from_json(data)

    def get_comment(self, posting_id: str, comment_id: str, with_source: bool = False) -> types.CommentInfo:
        """
        Get an individual comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param with_source: include source text of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call(
            "get_comment", location, method="GET", params=params, bodies=True, schema=schemas.COMMENT_INFO_SCHEMA
        )
        return types.CommentInfo.from_json(data)

    def update_all_comments(self, posting_id: str, attributes: types.CommentMassAttributes) -> types.Result:
        """
        Update operation overrides for all comments in the posting.

        :param posting_id: ID of the posting
        :param attributes:
        """
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        data = self.call("update_all_comments", location, method="PUT", body=attributes, schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def update_comment(self, posting_id: str, comment_id: str, comment: types.CommentText) -> types.CommentInfo:
        """
        Update the comment, creating a new revision of it. The text is processed just like in the ``POST`` request.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param comment:
        """
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "update_comment", location, method="PUT", src_bodies=True, body=comment, bodies=True,
            schema=schemas.COMMENT_INFO_SCHEMA
        )
        return types.CommentInfo.from_json(data)

    def delete_comment(self, posting_id: str, comment_id: str) -> types.CommentTotalInfo:
        """
        Delete the comment. The comment may not be purged from the database immediately, but preserved for some period
        of time to give a chance to restore it.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_comment", location, method="DELETE", schema=schemas.COMMENT_TOTAL_INFO_SCHEMA)
        return types.CommentTotalInfo.from_json(data)

    def get_postings_attached_to_comment(self, posting_id: str, comment_id: str) -> List[types.PostingInfo]:
        """
        Get all postings linked to media attached to the given comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}/attached".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_postings_attached_to_comment", location, method="GET", bodies=True,
            schema=schemas.POSTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.PostingInfo)

    def get_comment_revisions(self, posting_id: str, comment_id: str) -> List[types.CommentRevisionInfo]:
        """
        Get all revisions of the comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}/revisions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_comment_revisions", location, method="GET", bodies=True,
            schema=schemas.COMMENT_REVISION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.CommentRevisionInfo)

    def get_comment_revision(self, posting_id: str, comment_id: str, id: str) -> types.CommentRevisionInfo:
        """
        Get an individual revision of the comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param id: ID of the revision
        """
        location = "/postings/{postingId}/comments/{commentId}/revisions/{id}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), id=quote_plus(id)
        )
        data = self.call(
            "get_comment_revision", location, method="GET", bodies=True, schema=schemas.COMMENT_REVISION_INFO_SCHEMA
        )
        return types.CommentRevisionInfo.from_json(data)

    def create_comment_reaction(
        self, posting_id: str, comment_id: str, reaction: types.ReactionDescription
    ) -> types.ReactionCreated:
        """
        Add a reaction to the given comment. The reaction owner must authenticate in some way. Only one reaction is
        allowed from each owner to a particular comment. If a reaction from the same owner to this comment already
        exists, it is overwritten. If the reaction is not signed, the reaction will be kept for a limited period of
        time and then erased (the previous reaction of the same owner will be restored, if any).

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param reaction:
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "create_comment_reaction", location, method="POST", body=reaction, schema=schemas.REACTION_CREATED_SCHEMA
        )
        return types.ReactionCreated.from_json(data)

    def update_comment_reaction(
        self, posting_id: str, comment_id: str, owner_name: str, reaction: types.ReactionOverride
    ) -> types.ReactionInfo:
        """
        Update the reaction's operations or set operations' overrides.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param owner_name: reaction owner node name
        :param reaction:
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "update_comment_reaction", location, method="PUT", body=reaction, schema=schemas.REACTION_INFO_SCHEMA
        )
        return types.ReactionInfo.from_json(data)

    def get_comment_reactions_slice(
        self, posting_id: str, comment_id: str, negative: bool | None = None, emoji: int | None = None,
        before: int | None = None, limit: int | None = None
    ) -> types.ReactionsSliceInfo:
        """
        Get a slice of the list of reactions to the given comment, optionally filtered by reaction type, delimited by
        ``before`` moment and the given ``limit``. If ``before`` is not provided, the latest reactions are returned.
        The node may decide to return fewer reactions than the given ``limit``. The reactions are always sorted by
        moment, descending.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param negative: ``True``, to filter negative reactions, ``False``, to filter positive ones
        :param emoji: filter by reaction code, usually interpreted by clients as emoji code point
        :param before: filter reactions created at or before this moment
        :param limit: maximum number of reactions returned
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        params = {"negative": negative, "emoji": emoji, "before": before, "limit": limit}
        data = self.call(
            "get_comment_reactions_slice", location, method="GET", params=params,
            schema=schemas.REACTIONS_SLICE_INFO_SCHEMA
        )
        return types.ReactionsSliceInfo.from_json(data)

    def get_comment_reaction(self, posting_id: str, comment_id: str, owner_name: str) -> types.ReactionInfo:
        """
        Get the detailed information about the reaction of the given owner to the given comment. If no reaction with
        such an owner exists, an empty structure with just ``commentId`` is returned.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param owner_name: reaction owner node name
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call("get_comment_reaction", location, method="GET", schema=schemas.REACTION_INFO_SCHEMA)
        return types.ReactionInfo.from_json(data)

    def delete_all_comment_reactions(self, posting_id: str, comment_id: str) -> types.Result:
        """
        Delete all reactions to the given comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_all_comment_reactions", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def delete_comment_reaction(self, posting_id: str, comment_id: str, owner_name: str) -> types.ReactionTotalsInfo:
        """
        Delete the reaction of the given owner to the given comment.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        :param owner_name: reaction owner node name
        """
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "delete_comment_reaction", location, method="DELETE", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo.from_json(data)

    def get_comment_reaction_totals(self, posting_id: str, comment_id: str) -> types.ReactionTotalsInfo:
        """
        Get a summary of reactions to the comment given.

        :param posting_id: ID of the posting
        :param comment_id: ID of the comment
        """
        location = "/postings/{postingId}/comments/{commentId}/reaction-totals".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_comment_reaction_totals", location, method="GET", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo.from_json(data)

    def get_contacts(self, query: str | None = None, limit: int | None = None) -> List[types.ContactInfo]:
        """
        Search for contacts matching the search ``query``. Every space-delimited word in the query must match
        case-insensitively a beginning of the contact's node name or a beginning of any space-delimited word in the
        contact's full name. The order of words is not significant.
        
        The node may decide to return fewer contacts than the given ``limit``.
        
        The contacts are sorted by their *closeness* to the node, which is calculated from the number of reactions and
        comments and their age.

        :param query: the search query
        :param limit: maximum number of contacts returned
        """
        location = "/people/contacts".format()
        params = {"query": query, "limit": limit}
        data = self.call(
            "get_contacts", location, method="GET", params=params, schema=schemas.CONTACT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ContactInfo)

    def check_credentials(self) -> types.CredentialsCreated:
        """
        Check whether the credentials are initialized already.
        """
        location = "/credentials"
        data = self.call(
            "check_credentials", location, method="GET", auth=False, schema=schemas.CREDENTIALS_CREATED_SCHEMA
        )
        return types.CredentialsCreated.from_json(data)

    def create_credentials(self, credentials: types.Credentials) -> types.Result:
        """
        Initialize credentials if they are not set yet. Note that this operation can be executed without
        authentication, so this should be done as soon as possible after the node installation. Sign in is not allowed
        until the credentials are set.

        :param credentials:
        """
        location = "/credentials"
        data = self.call(
            "create_credentials", location, method="POST", body=credentials, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def update_credentials(self, credentials: types.CredentialsChange) -> types.Result:
        """
        Update credentials. Either old password or credentials reset token should be set in the input for the operation
        to succeed. Credentials reset token is not related to the authentication token and usually is sent to the user
        by E-mail.

        :param credentials:
        """
        location = "/credentials"
        data = self.call(
            "update_credentials", location, method="PUT", body=credentials, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def delete_credentials(self) -> types.Result:
        """
        Delete credentials.
        """
        location = "/credentials"
        data = self.call("delete_credentials", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def reset_credentials(self) -> types.EmailHint:
        """
        The node generates credentials reset token that is sent to the node admin by E-mail or using any other way that
        is defined for recovery of credentials. This token then may be used to change the credentials without knowing
        the password.
        """
        location = "/credentials/reset"
        data = self.call("reset_credentials", location, method="POST", auth=False, schema=schemas.EMAIL_HINT_SCHEMA)
        return types.EmailHint.from_json(data)

    def get_deleted_postings(self, page: int | None = None, limit: int | None = None) -> List[types.PostingInfo]:
        """
        Get the list of deleted postings, page by page. The node may decide to use a smaller page size than the given
        ``limit``. The postings are always sorted by the deletion timestamp, descending.

        :param page: page number, 0 by default
        :param limit: page size (maximum number of postings returned), the default is defined by the node
        """
        location = "/deleted-postings".format()
        params = {"page": page, "limit": limit}
        data = self.call(
            "get_deleted_postings", location, method="GET", params=params, bodies=True,
            schema=schemas.POSTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.PostingInfo)

    def get_deleted_posting(self, id: str) -> types.PostingInfo:
        """
        Get an individual deleted posting.

        :param id: ID of the posting
        """
        location = "/deleted-postings/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_deleted_posting", location, method="GET", bodies=True, schema=schemas.POSTING_INFO_SCHEMA
        )
        return types.PostingInfo.from_json(data)

    def restore_deleted_posting(self, id: str) -> types.PostingInfo:
        """
        Restore a posting. A new revision is created with the same content as in the latest revision.

        :param id: ID of the posting
        """
        location = "/deleted-postings/{id}/restore".format(id=quote_plus(id))
        data = self.call(
            "restore_deleted_posting", location, method="POST", bodies=True, schema=schemas.POSTING_INFO_SCHEMA
        )
        return types.PostingInfo.from_json(data)

    def get_delete_posting_revisions(
        self, posting_id: str, limit: int | None = None
    ) -> List[types.PostingRevisionInfo]:
        """
        Get all revisions of the deleted posting, but not more than ``limit``. The node may decide to return fewer
        revisions than the given ``limit``.

        :param posting_id: ID of the posting
        :param limit: maximum number of revisions returned
        """
        location = "/deleted-postings/{postingId}/revisions".format(postingId=quote_plus(posting_id))
        params = {"limit": limit}
        data = self.call(
            "get_delete_posting_revisions", location, method="GET", params=params, bodies=True,
            schema=schemas.POSTING_REVISION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.PostingRevisionInfo)

    def get_deleted_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        """
        Get an individual revision of the deleted posting.

        :param posting_id: ID of the posting
        :param id: ID of the revision
        """
        location = "/deleted-postings/{postingId}/revisions/{id}".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "get_deleted_posting_revision", location, method="GET", bodies=True,
            schema=schemas.POSTING_REVISION_INFO_SCHEMA
        )
        return types.PostingRevisionInfo.from_json(data)

    def restore_deleted_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        """
        Restore a posting at a particular revision. A new revision is created with the same content as in the given
        revision.

        :param posting_id: ID of the posting
        :param id: ID of the revision
        """
        location = "/postings/{postingId}/revisions/{id}/restore".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "restore_deleted_posting_revision", location, method="POST", bodies=True,
            schema=schemas.POSTING_REVISION_INFO_SCHEMA
        )
        return types.PostingRevisionInfo.from_json(data)

    def get_domains(self) -> List[types.DomainInfo]:
        """
        Get the list of registered domains.
        """
        location = "/domains"
        data = self.call("get_domains", location, method="GET", schema=schemas.DOMAIN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.DomainInfo)

    def get_domain(self, name: str) -> types.DomainInfo:
        """
        Get information about the domain with the given hostname. If domain registration for this server is public,
        this request does not require authentication.

        :param name: domain name
        """
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("get_domain", location, method="GET", schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo.from_json(data)

    def create_domain(self, domain: types.DomainAttributes) -> types.DomainInfo:
        """
        Create a new domain with the given hostname. If ``nodeId`` is not passed, it is generated automatically. If
        domain registration for this server is public, this request does not require authentication.

        :param domain:
        """
        location = "/domains"
        data = self.call("create_domain", location, method="POST", body=domain, schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo.from_json(data)

    def update_domain(self, name: str, domain: types.DomainAttributes) -> types.DomainInfo:
        """
        Update the domain with the given hostname. If the new hostname is not passed, the old hostname is preserved.
        (Note that you cannot pass a new name for the default hostname, because it cannot be renamed and ``_default_``
        is not a valid hostname. Skip this field if you want to update the default hostname.) If ``nodeId`` is not
        passed, it is generated automatically.

        :param name: domain's hostname
        :param domain:
        """
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("update_domain", location, method="PUT", body=domain, schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo.from_json(data)

    def delete_domain(self, name: str) -> types.Result:
        """
        Delete the domain with the given hostname. This operation deletes the domain record only, the user's data
        related to the domain is preserved.

        :param name: domain name
        """
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("delete_domain", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def is_domain_available(self, node_name: str) -> types.DomainAvailable:
        """
        Get an available domain name recommended for the given node name. The domain name is usually chosen to be close
        to the node name in English transcription. If domain registration for this server is not public, this request
        is not accessible.

        :param node_name: node name
        """
        location = "/domains/available".format()
        params = {"nodeName": node_name}
        data = self.call(
            "is_domain_available", location, method="GET", auth=False, params=params,
            schema=schemas.DOMAIN_AVAILABLE_SCHEMA
        )
        return types.DomainAvailable.from_json(data)

    def get_drafts(
        self, draft_type: types.DraftType, node_name: str, posting_id: str | None = None, comment_id: str | None = None,
        page: int | None = None, limit: int | None = None
    ) -> List[types.DraftInfo]:
        """
        Get the list of drafts, page by page, filtered by the given criteria. The node may decide to use a smaller page
        size than the given ``limit``. The drafts are always sorted by the creation timestamp, descending.

        :param draft_type: type of the drafts
        :param node_name: name of the node the drafts are related to
        :param posting_id: ID of the posting, mandatory for all types, except ``new-posting``
        :param comment_id: ID of the comment, mandatory for ``comment-update`` type
        :param page: page number, 0 by default
        :param limit: page size (maximum number of postings returned), the default is defined by the node
        """
        location = "/drafts".format()
        params = {
            "draftType": draft_type, "nodeName": node_name, "postingId": posting_id, "commentId": comment_id,
            "page": page, "limit": limit
        }
        data = self.call(
            "get_drafts", location, method="GET", params=params, bodies=True, schema=schemas.DRAFT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.DraftInfo)

    def create_draft(self, draft: types.DraftText) -> types.DraftInfo:
        """
        Create a new draft from the text given.

        :param draft:
        """
        location = "/drafts"
        data = self.call(
            "create_draft", location, method="POST", src_bodies=True, body=draft, bodies=True,
            schema=schemas.DRAFT_INFO_SCHEMA
        )
        return types.DraftInfo.from_json(data)

    def get_draft(self, id: str) -> types.DraftInfo:
        """
        Get an individual draft.

        :param id: ID of the draft
        """
        location = "/drafts/{id}".format(id=quote_plus(id))
        data = self.call("get_draft", location, method="GET", bodies=True, schema=schemas.DRAFT_INFO_SCHEMA)
        return types.DraftInfo.from_json(data)

    def update_draft(self, id: str, draft: types.DraftText) -> types.DraftInfo:
        """
        Update the draft.

        :param id: ID of the draft
        :param draft:
        """
        location = "/drafts/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_draft", location, method="PUT", src_bodies=True, body=draft, bodies=True,
            schema=schemas.DRAFT_INFO_SCHEMA
        )
        return types.DraftInfo.from_json(data)

    def delete_draft(self, id: str) -> types.Result:
        """
        Delete the draft.

        :param id: ID of the draft
        """
        location = "/drafts/{id}".format(id=quote_plus(id))
        data = self.call("delete_draft", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def get_features(self) -> types.Features:
        """
        Get information about features supported by the node.
        """
        location = "/features"
        data = self.call("get_features", location, method="GET", schema=schemas.FEATURES_SCHEMA)
        return types.Features.from_json(data)

    def get_feeds(self) -> List[types.FeedInfo]:
        """
        Get general information about all feeds accessible by client.
        """
        location = "/feeds"
        data = self.call("get_feeds", location, method="GET", schema=schemas.FEED_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FeedInfo)

    def get_feed_general(self, feed_name: str) -> types.FeedInfo:
        """
        Get general information about the feed.

        :param feed_name: name of the feed
        """
        location = "/feeds/{feedName}".format(feedName=quote_plus(feed_name))
        data = self.call("get_feed_general", location, method="GET", schema=schemas.FEED_INFO_SCHEMA)
        return types.FeedInfo.from_json(data)

    def get_feed_status(self, feed_name: str) -> types.FeedStatus:
        """
        Get information about the total number and number of non-read and non-viewed stories in the feed.

        :param feed_name: name of the feed
        """
        location = "/feeds/{feedName}/status".format(feedName=quote_plus(feed_name))
        data = self.call("get_feed_status", location, method="GET", schema=schemas.FEED_STATUS_SCHEMA)
        return types.FeedStatus.from_json(data)

    def update_feed_status(self, feed_name: str, change: types.FeedStatusChange) -> types.FeedStatus:
        """
        Update information about non-read and non-viewed stories in the feed.

        :param feed_name: name of the feed
        :param change:
        """
        location = "/feeds/{feedName}/status".format(feedName=quote_plus(feed_name))
        data = self.call("update_feed_status", location, method="PUT", body=change, schema=schemas.FEED_STATUS_SCHEMA)
        return types.FeedStatus.from_json(data)

    def get_feed_slice(
        self, feed_name: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.FeedSliceInfo:
        """
        Get a slice of the feed, delimited by ``before`` or ``after`` moments (but not both) and the given ``limit``.
        If neither ``before`` nor ``after`` are provided, the latest stories are returned. The node may decide to
        return fewer stories than the given ``limit``. The stories are always sorted by moment, descending.

        :param feed_name: name of the feed
        :param after: filter stories posted strongly after this moment
        :param before: filter stories posted at or before this moment
        :param limit: maximum number of stories returned
        """
        location = "/feeds/{feedName}/stories".format(feedName=quote_plus(feed_name))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_feed_slice", location, method="GET", params=params, bodies=True, schema=schemas.FEED_SLICE_INFO_SCHEMA
        )
        return types.FeedSliceInfo.from_json(data)

    def get_friend_groups(self) -> List[types.FriendGroupInfo]:
        """
        Get the list of all groups of friends that exist on the node.
        """
        location = "/people/friends/groups"
        data = self.call("get_friend_groups", location, method="GET", schema=schemas.FRIEND_GROUP_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendGroupInfo)

    def get_friend_group(self, id: str) -> types.FriendGroupInfo:
        """
        Get the information about the group of friends.

        :param id: ID of the group of friends
        """
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call("get_friend_group", location, method="GET", schema=schemas.FRIEND_GROUP_INFO_SCHEMA)
        return types.FriendGroupInfo.from_json(data)

    def create_friend_group(self, friend_group: types.FriendGroupDescription) -> types.FriendGroupInfo:
        """
        Create a group of friends.

        :param friend_group:
        """
        location = "/people/friends/groups"
        data = self.call(
            "create_friend_group", location, method="POST", body=friend_group, schema=schemas.FRIEND_GROUP_INFO_SCHEMA
        )
        return types.FriendGroupInfo.from_json(data)

    def update_friend_group(self, id: str, friend_group: types.FriendGroupDescription) -> types.FriendGroupInfo:
        """
        Update the details of the group of friends.

        :param id: ID of the group of friends
        :param friend_group:
        """
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_friend_group", location, method="PUT", body=friend_group, schema=schemas.FRIEND_GROUP_INFO_SCHEMA
        )
        return types.FriendGroupInfo.from_json(data)

    def delete_friend_group(self, id: str) -> types.Result:
        """
        Delete the group of friends.

        :param id: ID of the group of friends
        """
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call("delete_friend_group", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def get_friends(self, group_id: str | None = None) -> List[types.FriendInfo]:
        """
        Get the list of all friends of the node or friends belonging to a particular group.

        :param group_id: ID of a group of friends
        """
        location = "/people/friends".format()
        params = {"groupId": group_id}
        data = self.call("get_friends", location, method="GET", params=params, schema=schemas.FRIEND_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendInfo)

    def get_friend(self, name: str) -> types.FriendInfo:
        """
        Get the friendship information for the node given.

        :param name: name of the node
        """
        location = "/people/friends/{name}".format(name=quote_plus(name))
        data = self.call("get_friend", location, method="GET", schema=schemas.FRIEND_INFO_SCHEMA)
        return types.FriendInfo.from_json(data)

    def update_friends(self, friends: List[types.FriendDescription]) -> List[types.FriendInfo]:
        """
        Update the friendship status of the nodes passed in the input. If some node passed in the input is not a member
        of some of the groups of friends listed for it, the node is added to them. If it is a member of some groups of
        friends that are not listed for it, the node is removed from them.

        :param friends:
        """
        location = "/people/friends"
        data = self.call(
            "update_friends", location, method="PUT", body=friends, schema=schemas.FRIEND_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.FriendInfo)

    def get_friend_ofs(self) -> List[types.FriendOfInfo]:
        """
        Get the list of all nodes that added this node to their friends.
        """
        location = "/people/friend-ofs"
        data = self.call("get_friend_ofs", location, method="GET", schema=schemas.FRIEND_OF_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendOfInfo)

    def get_friend_of(self, name: str) -> types.FriendOfInfo:
        """
        Get the information for the node given, whether it has added this node to its friends.

        :param name: name of the node
        """
        location = "/people/friend-ofs/{name}".format(name=quote_plus(name))
        data = self.call("get_friend_of", location, method="GET", schema=schemas.FRIEND_OF_INFO_SCHEMA)
        return types.FriendOfInfo.from_json(data)

    def upload_private_media(self, file: IO, file_type: str) -> types.PrivateMediaFileInfo:
        """
        Upload a new media file. Content of the file is passed in the request body

        :param file:
        :param file_type: content-type of ``file``
        """
        location = "/media/private"
        data = self.call(
            "upload_private_media", location, method="POST", body_file=file, body_file_type=file_type,
            schema=schemas.PRIVATE_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PrivateMediaFileInfo.from_json(data)

    def get_private_media(self, id: str, width: int | None = None, download: bool | None = None) -> IO:
        """
        Get media file content (returned in the response body).

        :param id: media file ID
        :param width: preferred width of the media in pixels; if present, the node will try to return the smallest
            in size, but the best in quality variant of the media, according to the width provided
        :param download: if ``True``, the node will add ``Content-Disposition: attachment`` header to the output
        """
        location = "/media/private/{id}/data".format(id=quote_plus(id))
        params = {"width": width, "download": download}
        data = self.call("get_private_media", location, method="GET", params=params, schema="blob")
        return cast(IO, data)

    def get_private_media_info(self, id: str) -> types.PrivateMediaFileInfo:
        """
        Get media file details.

        :param id: media file ID
        """
        location = "/media/private/{id}/info".format(id=quote_plus(id))
        data = self.call(
            "get_private_media_info", location, method="GET", schema=schemas.PRIVATE_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PrivateMediaFileInfo.from_json(data)

    def get_private_media_parent_entry(self, id: str) -> List[types.EntryInfo]:
        """
        Get the list of all postings and comments the media file is attached to.

        :param id: media file ID
        """
        location = "/media/private/{id}/parent".format(id=quote_plus(id))
        data = self.call(
            "get_private_media_parent_entry", location, method="GET", bodies=True,
            schema=schemas.ENTRY_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.EntryInfo)

    def upload_public_media(self, file: IO, file_type: str) -> types.PublicMediaFileInfo:
        """
        Upload a new media file. The content of the file is passed in the request body

        :param file:
        :param file_type: content-type of ``file``
        """
        location = "/media/public"
        data = self.call(
            "upload_public_media", location, method="POST", body_file=file, body_file_type=file_type,
            schema=schemas.PUBLIC_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PublicMediaFileInfo.from_json(data)

    def get_public_media(self, id: str, width: int | None = None, download: bool | None = None) -> IO:
        """
        Get media file content (returned in the response body).

        :param id: media file ID
        :param width: preferred width of the media in pixels; if present, the node will try to return the smallest
            in size, but the best in quality variant of the media, according to the width provided
        :param download: if ``True``, the node will add ``Content-Disposition: attachment`` header to the output
        """
        location = "/media/public/{id}/data".format(id=quote_plus(id))
        params = {"width": width, "download": download}
        data = self.call("get_public_media", location, method="GET", auth=False, params=params, schema="blob")
        return cast(IO, data)

    def get_public_media_info(self, id: str) -> types.PublicMediaFileInfo:
        """
        Get media file details.

        :param id: media file ID
        """
        location = "/media/public/{id}/info".format(id=quote_plus(id))
        data = self.call(
            "get_public_media_info", location, method="GET", auth=False, schema=schemas.PUBLIC_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PublicMediaFileInfo.from_json(data)

    def get_node_name(self) -> types.NodeNameInfo:
        """
        Get the name of the node. Admin user receives the current status of the latest operation with the node name.
        """
        location = "/node-name"
        data = self.call("get_node_name", location, method="GET", schema=schemas.NODE_NAME_INFO_SCHEMA)
        return types.NodeNameInfo.from_json(data)

    def create_node_name(self, name_to_register: types.NameToRegister) -> types.RegisteredNameSecret:
        """
        Register a new name for the node. The corresponding signing key is generated automatically and stored at the
        node. The updating key is generated and returned in the encoded form and in the form of mnemonic (a sequence of
        English words). The words need to be written down and stored securely to be able to perform further operations
        with the name.

        :param name_to_register:
        """
        location = "/node-name"
        data = self.call(
            "create_node_name", location, method="POST", body=name_to_register,
            schema=schemas.REGISTERED_NAME_SECRET_SCHEMA
        )
        return types.RegisteredNameSecret.from_json(data)

    def update_node_name(self, secret: types.RegisteredNameSecret) -> types.Result:
        """
        Update the name of the node. May be used to assign an already-registered name to the node (the corresponding
        signing key is generated automatically and stored at the node), or to prolong the name. The secret or mnemonic
        of the updating key must be provided for this operation.

        :param secret:
        """
        location = "/node-name"
        data = self.call("update_node_name", location, method="PUT", body=secret, schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def delete_node_name(self) -> types.Result:
        """
        Delete all the information related to the node name (including the signing key) from the node. The name record
        on the naming server is not touched.
        """
        location = "/node-name"
        data = self.call("delete_node_name", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def send_notification(self, packet: types.NotificationPacket) -> types.Result:
        """
        Accept a notification packet from another node. Notification packets older than 10 minutes are ignored. The
        sending node should update the packet timestamp and the signature and send the packet again. This mechanism
        prevents attackers from recording and resending old signed packets.

        :param packet:
        """
        location = "/notifications"
        data = self.call(
            "send_notification", location, method="POST", body=packet, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def get_people_general(self) -> types.PeopleGeneralInfo:
        """
        Get general information about other nodes.
        """
        location = "/people"
        data = self.call("get_people_general", location, method="GET", schema=schemas.PEOPLE_GENERAL_INFO_SCHEMA)
        return types.PeopleGeneralInfo.from_json(data)

    def register_plugin(self, plugin: types.PluginDescription) -> types.PluginInfo:
        """
        Register the plugin. If the plugin authenticates as root admin, the plugin is registered at the server level.
        If the plugin authenticates as node admin, the plugin is registered at the node level.

        :param plugin:
        """
        location = "/plugins"
        data = self.call("register_plugin", location, method="POST", body=plugin, schema=schemas.PLUGIN_INFO_SCHEMA)
        return types.PluginInfo.from_json(data)

    def get_plugins(self) -> List[types.PluginInfo]:
        """
        Get information about all plugins registered for the node and server.
        """
        location = "/plugins"
        data = self.call("get_plugins", location, method="GET", schema=schemas.PLUGIN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.PluginInfo)

    def get_plugin(self, plugin_name: str) -> types.PluginInfo:
        """
        Get information about the plugin.

        :param plugin_name: name of the plugin
        """
        location = "/plugins/{pluginName}".format(pluginName=quote_plus(plugin_name))
        data = self.call("get_plugin", location, method="GET", schema=schemas.PLUGIN_INFO_SCHEMA)
        return types.PluginInfo.from_json(data)

    def unregister_plugin(self, plugin_name: str) -> types.Result:
        """
        Unregister the plugin.

        :param plugin_name: name of the plugin
        """
        location = "/plugins/{pluginName}".format(pluginName=quote_plus(plugin_name))
        data = self.call("unregister_plugin", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def create_posting(self, posting: types.PostingText) -> types.PostingInfo:
        """
        Create a new posting from the text given and publish it in the given feeds (if any). The heading and the
        preview of the posting are created automatically, if needed. The posting owner must authenticate in some way.
        If the posting is not signed, it will be kept for a limited period of time and then erased. If authenticated as
        admin, the node signs the posting.

        :param posting:
        """
        location = "/postings"
        data = self.call(
            "create_posting", location, method="POST", src_bodies=True, body=posting, bodies=True,
            schema=schemas.POSTING_INFO_SCHEMA
        )
        return types.PostingInfo.from_json(data)

    def update_posting(self, id: str, posting: types.PostingText) -> types.PostingInfo:
        """
        Update the posting, creating a new revision of it. The text is processed just like in the ``POST`` request.

        :param id: ID of the posting
        :param posting:
        """
        location = "/postings/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_posting", location, method="PUT", src_bodies=True, body=posting, bodies=True,
            schema=schemas.POSTING_INFO_SCHEMA
        )
        return types.PostingInfo.from_json(data)

    def get_posting(self, id: str, with_source: bool = False) -> types.PostingInfo:
        """
        Get an individual posting.

        :param id: ID of the posting
        :param with_source: include source text of the posting
        """
        location = "/postings/{id}".format(id=quote_plus(id))
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call(
            "get_posting", location, method="GET", params=params, bodies=True, schema=schemas.POSTING_INFO_SCHEMA
        )
        return types.PostingInfo.from_json(data)

    def delete_posting(self, id: str) -> types.Result:
        """
        Delete the posting. The posting may not be purged from the database immediately, but preserved for some period
        of time to give a chance to restore it.

        :param id: ID of the posting
        """
        location = "/postings/{id}".format(id=quote_plus(id))
        data = self.call("delete_posting", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def get_postings_attached_to_posting(self, id: str) -> List[types.PostingInfo]:
        """
        Get all postings linked to media attached to the given posting.

        :param id: ID of the posting
        """
        location = "/postings/{id}/attached".format(id=quote_plus(id))
        data = self.call(
            "get_postings_attached_to_posting", location, method="GET", bodies=True,
            schema=schemas.POSTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.PostingInfo)

    def get_posting_revisions(self, posting_id: str, limit: int | None = None) -> List[types.PostingRevisionInfo]:
        """
        Get all revisions of the posting, but not more than ``limit``. The node may decide to return fewer revisions
        than the given ``limit``.

        :param posting_id: ID of the posting
        :param limit: maximum number of revisions returned
        """
        location = "/postings/{postingId}/revisions".format(postingId=quote_plus(posting_id))
        params = {"limit": limit}
        data = self.call(
            "get_posting_revisions", location, method="GET", params=params, bodies=True,
            schema=schemas.POSTING_REVISION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.PostingRevisionInfo)

    def get_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        """
        Get an individual revision of the posting.

        :param posting_id: ID of the posting
        :param id: ID of the revision
        """
        location = "/postings/{postingId}/revisions/{id}".format(postingId=quote_plus(posting_id), id=quote_plus(id))
        data = self.call(
            "get_posting_revision", location, method="GET", bodies=True, schema=schemas.POSTING_REVISION_INFO_SCHEMA
        )
        return types.PostingRevisionInfo.from_json(data)

    def restore_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        """
        Restore a revision of the posting. A new revision is created with the same content as in the given revision.

        :param posting_id: ID of the posting
        :param id: ID of the revision
        """
        location = "/postings/{postingId}/revisions/{id}/restore".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "restore_posting_revision", location, method="POST", bodies=True,
            schema=schemas.POSTING_REVISION_INFO_SCHEMA
        )
        return types.PostingRevisionInfo.from_json(data)

    def create_posting_reaction(self, posting_id: str, reaction: types.ReactionDescription) -> types.ReactionCreated:
        """
        Add a reaction to the given posting. The reaction owner must authenticate in some way. Only one reaction is
        allowed from each owner to a particular posting. If a reaction from the same owner to this posting already
        exists, it is overwritten. If the reaction is not signed, the reaction will be kept for a limited period of
        time and then erased (the previous reaction of the same owner will be restored, if any).

        :param posting_id: ID of the posting
        :param reaction:
        """
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        data = self.call(
            "create_posting_reaction", location, method="POST", body=reaction, schema=schemas.REACTION_CREATED_SCHEMA
        )
        return types.ReactionCreated.from_json(data)

    def get_posting_reactions_slice(
        self, posting_id: str, negative: bool | None = None, emoji: int | None = None, before: int | None = None,
        limit: int | None = None
    ) -> types.ReactionsSliceInfo:
        """
        Get a slice of the list of reactions to the given posting, optionally filtered by reaction type, delimited by
        ``before`` moment and the given ``limit``. If ``before`` is not provided, the latest reactions are returned.
        The node may decide to return less reactions than the given ``limit``. The reactions are always sorted by
        moment, descending.

        :param posting_id: ID of the posting
        :param negative: ``True``, to filter negative reactions, ``False``, to filter positive ones
        :param emoji: filter by reaction code, usually interpreted by clients as emoji code point
        :param before: filter reactions created at or before this moment
        :param limit: maximum number of reactions returned
        """
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        params = {"negative": negative, "emoji": emoji, "before": before, "limit": limit}
        data = self.call(
            "get_posting_reactions_slice", location, method="GET", params=params,
            schema=schemas.REACTIONS_SLICE_INFO_SCHEMA
        )
        return types.ReactionsSliceInfo.from_json(data)

    def update_posting_reaction(
        self, posting_id: str, owner_name: str, reaction: types.ReactionOverride
    ) -> types.ReactionInfo:
        """
        Update the reaction's operations or set operations' overrides.

        :param posting_id: ID of the posting
        :param owner_name: reaction owner node name
        :param reaction:
        """
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "update_posting_reaction", location, method="PUT", body=reaction, schema=schemas.REACTION_INFO_SCHEMA
        )
        return types.ReactionInfo.from_json(data)

    def get_posting_reaction(self, posting_id: str, owner_name: str) -> types.ReactionInfo:
        """
        Get the detailed information about the reaction of the given owner to the given posting. If no reaction with
        such an owner exists, an empty structure with just ``postingId`` is returned.

        :param posting_id: ID of the posting
        :param owner_name: reaction owner node name
        """
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call("get_posting_reaction", location, method="GET", schema=schemas.REACTION_INFO_SCHEMA)
        return types.ReactionInfo.from_json(data)

    def delete_all_posting_reactions(self, posting_id: str) -> types.Result:
        """
        Delete all reactions to the given posting.

        :param posting_id: ID of the posting
        """
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        data = self.call("delete_all_posting_reactions", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def delete_posting_reaction(self, posting_id: str, owner_name: str) -> types.ReactionTotalsInfo:
        """
        Delete the reaction of the given owner to the given posting.

        :param posting_id: ID of the posting
        :param owner_name: reaction owner node name
        """
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "delete_posting_reaction", location, method="DELETE", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo.from_json(data)

    def search_posting_reactions(self, filter: types.ReactionsFilter) -> List[types.ReactionInfo]:
        """
        Search reactions by criteria provided. Both reaction owner and at least one posting ID should be provided to
        search, otherwise an empty list is returned.

        :param filter:
        """
        location = "/postings/reactions/search"
        data = self.call(
            "search_posting_reactions", location, method="POST", body=filter, schema=schemas.REACTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ReactionInfo)

    def get_posting_reaction_totals(self, posting_id: str) -> types.ReactionTotalsInfo:
        """
        Get a summary of reactions to the posting given.

        :param posting_id: ID of the posting
        """
        location = "/postings/{postingId}/reaction-totals".format(postingId=quote_plus(posting_id))
        data = self.call(
            "get_posting_reaction_totals", location, method="GET", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo.from_json(data)

    def search_posting_reaction_totals(self, filter: types.ReactionTotalsFilter) -> List[types.ReactionTotalsInfo]:
        """
        Search summaries of reactions by criteria provided. At least one posting ID should be provided to search,
        otherwise an empty list is returned.

        :param filter:
        """
        location = "/postings/reaction-totals/search"
        data = self.call(
            "search_posting_reaction_totals", location, method="POST", body=filter,
            schema=schemas.REACTION_TOTALS_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ReactionTotalsInfo)

    def get_profile(self, with_source: bool = False) -> types.ProfileInfo:
        """
        Get the profile.

        :param with_source: include source text of the bio
        """
        location = "/profile".format()
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call("get_profile", location, method="GET", params=params, schema=schemas.PROFILE_INFO_SCHEMA)
        return types.ProfileInfo.from_json(data)

    def update_profile(self, profile: types.ProfileAttributes) -> types.ProfileInfo:
        """
        Update the profile. Fields that are not set in the request body are left intact. Fields that are set to an
        empty value are reset to their defaults.

        :param profile:
        """
        location = "/profile"
        data = self.call("update_profile", location, method="PUT", body=profile, schema=schemas.PROFILE_INFO_SCHEMA)
        return types.ProfileInfo.from_json(data)

    def get_delete_node_request_status(self) -> types.DeleteNodeStatus:
        """
        Get the current status of the request to delete the node.
        """
        location = "/provider/delete-node"
        data = self.call(
            "get_delete_node_request_status", location, method="GET", schema=schemas.DELETE_NODE_STATUS_SCHEMA
        )
        return types.DeleteNodeStatus.from_json(data)

    def send_delete_node_request(self, delete_node_text: types.DeleteNodeText) -> types.DeleteNodeStatus:
        """
        Send a request to the provider to delete the node.

        :param delete_node_text:
        """
        location = "/provider/delete-node"
        data = self.call(
            "send_delete_node_request", location, method="POST", body=delete_node_text,
            schema=schemas.DELETE_NODE_STATUS_SCHEMA
        )
        return types.DeleteNodeStatus.from_json(data)

    def cancel_delete_node_request(self) -> types.DeleteNodeStatus:
        """
        Cancel the request to delete the node.
        """
        location = "/provider/delete-node"
        data = self.call(
            "cancel_delete_node_request", location, method="DELETE", schema=schemas.DELETE_NODE_STATUS_SCHEMA
        )
        return types.DeleteNodeStatus.from_json(data)

    def proxy_media(self, url: str) -> IO:
        """
        Open the URL passed in the parameters and pass to the client the media file returned by the server.

        :param url:
        """
        location = "/proxy/media".format()
        params = {"url": url}
        data = self.call("proxy_media", location, method="GET", params=params, schema="blob")
        return cast(IO, data)

    def proxy_link_preview(self, url: str) -> types.LinkPreviewInfo:
        """
        Parse the page located at the URL and return the title, the description and the picture that may be used to
        build a preview of the page.

        :param url:
        """
        location = "/proxy/link-preview".format()
        params = {"url": url}
        data = self.call(
            "proxy_link_preview", location, method="GET", params=params, schema=schemas.LINK_PREVIEW_INFO_SCHEMA
        )
        return types.LinkPreviewInfo.from_json(data)

    def register_at_push_relay(self, attributes: types.PushRelayClientAttributes) -> types.Result:
        """
        Register a client at the push relay server to receive messages from this node. The operation is synchronous.

        :param attributes:
        """
        location = "/push-relay"
        data = self.call(
            "register_at_push_relay", location, method="POST", body=attributes, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def ask_remote_node(self, node_name: str, details: types.AskDescription) -> types.Result:
        """
        Send a request to the remote node.

        :param node_name: name of the remote node
        :param details:
        """
        location = "/nodes/{nodeName}/ask".format(nodeName=quote_plus(node_name))
        data = self.call("ask_remote_node", location, method="POST", body=details, schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def create_remote_comment(
        self, node_name: str, posting_id: str, comment: types.CommentSourceText
    ) -> types.Result:
        """
        Add a comment to the posting on the remote node and register it in the registry at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment:
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call(
            "create_remote_comment", location, method="POST", src_bodies=True, body=comment,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def update_remote_comment(
        self, node_name: str, posting_id: str, comment_id: str, comment: types.CommentSourceText
    ) -> types.Result:
        """
        Update a comment to the posting on the remote node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        :param comment:
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "update_remote_comment", location, method="PUT", src_bodies=True, body=comment,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def delete_remote_comment(self, node_name: str, posting_id: str, comment_id: str) -> types.Result:
        """
        Delete a comment from the registry of all comments at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_remote_comment", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def verify_remote_comment(self, node_name: str, posting_id: str, comment_id: str) -> types.AsyncOperationCreated:
        """
        Verify the signature of the given comment to the posting on the remote node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "verify_remote_comment", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated.from_json(data)

    def create_remote_comment_reaction(
        self, node_name: str, posting_id: str, comment_id: str, reaction: types.ReactionAttributes
    ) -> types.Result:
        """
        Add a reaction to the comment on the remote node and register it in the registry at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        :param reaction:
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "create_remote_comment_reaction", location, method="POST", body=reaction, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def delete_remote_comment_reaction(self, node_name: str, posting_id: str, comment_id: str) -> types.Result:
        """
        Delete a reaction from the registry of all reactions at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_remote_comment_reaction", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def verify_remote_comment_reaction(
        self, node_name: str, posting_id: str, comment_id: str, owner_name: str
    ) -> types.AsyncOperationCreated:
        """
        Verify the signature of the reaction of the given owner to the comment on the remote node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param comment_id: ID of the comment on the remote node
        :param owner_name: reaction owner node name
        """
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions/{ownerName}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id),
            ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "verify_remote_comment_reaction", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated.from_json(data)

    def create_remote_posting(self, node_name: str, posting: types.PostingSourceText) -> types.Result:
        """
        Add a posting to the remote node and register it in the registry at the local node.

        :param node_name: name of the remote node
        :param posting:
        """
        location = "/nodes/{nodeName}/postings".format(nodeName=quote_plus(node_name))
        data = self.call(
            "create_remote_posting", location, method="POST", src_bodies=True, body=posting,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def update_remote_posting(
        self, node_name: str, posting_id: str, posting: types.PostingSourceText
    ) -> types.Result:
        """
        Update a posting on the remote node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param posting:
        """
        location = "/nodes/{nodeName}/postings/{postingId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call(
            "update_remote_posting", location, method="PUT", src_bodies=True, body=posting,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def delete_remote_posting(self, node_name: str, posting_id: str) -> types.Result:
        """
        Delete a posting from the registry of all remote postings at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        """
        location = "/nodes/{nodeName}/postings/{postingId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("delete_remote_posting", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def verify_remote_posting(self, node_name: str, id: str) -> types.AsyncOperationCreated:
        """
        Verify the signature of the given posting.

        :param node_name: name of the remote node
        :param id: ID of the posting on the remote node
        """
        location = "/nodes/{nodeName}/postings/{id}/verify".format(nodeName=quote_plus(node_name), id=quote_plus(id))
        data = self.call(
            "verify_remote_posting", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated.from_json(data)

    def verify_remote_posting_revision(
        self, node_name: str, id: str, revision_id: str
    ) -> types.AsyncOperationCreated:
        """
        Verify the signature of the given revision of a posting.

        :param node_name: name of the remote node
        :param id: ID of the posting on the remote node
        :param revision_id: ID of the posting revision
        """
        location = "/nodes/{nodeName}/postings/{id}/revisions/{revisionId}/verify".format(
            nodeName=quote_plus(node_name), id=quote_plus(id), revisionId=quote_plus(revision_id)
        )
        data = self.call(
            "verify_remote_posting_revision", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated.from_json(data)

    def create_remote_posting_reaction(
        self, node_name: str, posting_id: str, reaction: types.ReactionAttributes
    ) -> types.Result:
        """
        Add a reaction to the posting on the remote node and register it in the registry at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param reaction:
        """
        location = "/nodes/{nodeName}/postings/{postingId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call(
            "create_remote_posting_reaction", location, method="POST", body=reaction, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def delete_remote_posting_reaction(self, node_name: str, posting_id: str) -> types.Result:
        """
        Delete a reaction from the registry of all reactions at the local node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        """
        location = "/nodes/{nodeName}/postings/{postingId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("delete_remote_posting_reaction", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def verify_remote_posting_reaction(
        self, node_name: str, posting_id: str, owner_name: str
    ) -> types.AsyncOperationCreated:
        """
        Verify the signature of the reaction of the given owner to the posting on the remote node.

        :param node_name: name of the remote node
        :param posting_id: ID of the posting on the remote node
        :param owner_name: reaction owner node name
        """
        location = "/nodes/{nodeName}/postings/{postingId}/reactions/{ownerName}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "verify_remote_posting_reaction", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated.from_json(data)

    def create_remote_sheriff_order(
        self, node_name: str, sheriff_order: types.SheriffOrderAttributes
    ) -> types.Result:
        """
        Sign and send the order to the remote node and store it in the registry at the local node.

        :param node_name: name of the remote node
        :param sheriff_order:
        """
        location = "/nodes/{nodeName}/sheriff/orders".format(nodeName=quote_plus(node_name))
        data = self.call(
            "create_remote_sheriff_order", location, method="POST", body=sheriff_order, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def get_remote_sheriff_order(self, node_name: str, id: str) -> types.SheriffOrderInfo:
        """
        Get the details of the given sheriff's order

        :param node_name: name of the remote node
        :param id: ID of the order
        """
        location = "/nodes/{nodeName}/sheriff/orders/{id}".format(nodeName=quote_plus(node_name), id=quote_plus(id))
        data = self.call(
            "get_remote_sheriff_order", location, method="GET", auth=False, schema=schemas.SHERIFF_ORDER_INFO_SCHEMA
        )
        return types.SheriffOrderInfo.from_json(data)

    def update_settings(self, settings: List[types.SettingInfo]) -> types.Result:
        """
        Update the given settings. If the input contains node settings, they are validated and the first validation
        error is returned, if any. The update is always performed as a whole - if there is an error saving any one of
        the settings in the input, none of them are updated.
        
        If one of the settings to be updated is privileged, *root secret* authentication is required. If one of the
        settings to be updated is non-privileged, *admin* authentication is required.

        :param settings:
        """
        location = "/settings"
        data = self.call("update_settings", location, method="PUT", body=settings, schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def get_client_settings(self, prefix: str | None = None) -> List[types.SettingInfo]:
        """
        Get all client settings, sorted by name.

        :param prefix: filter settings whose names start with the given prefix, case-sensitive (``client.`` prefix
            must be included)
        """
        location = "/settings/client".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_client_settings", location, method="GET", params=params, schema=schemas.SETTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingInfo)

    def get_node_settings(self, prefix: str | None = None) -> List[types.SettingInfo]:
        """
        Get all node settings, sorted by name. If a setting has not changed its value from the default, it is omitted.

        :param prefix: filter settings whose names start with the given prefix, case-sensitive
        """
        location = "/settings/node".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_node_settings", location, method="GET", params=params, schema=schemas.SETTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingInfo)

    def get_node_settings_metadata(self, prefix: str | None = None) -> List[types.SettingMetaInfo]:
        """
        Get all node settings metadata, sorted by name.

        :param prefix: filter settings whose names start with the given prefix, case-sensitive
        """
        location = "/settings/node/metadata".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_node_settings_metadata", location, method="GET", params=params,
            schema=schemas.SETTING_META_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingMetaInfo)

    def update_node_settings_metadata(self, metadata: List[types.SettingMetaAttributes]) -> types.Result:
        """
        Update node settings metadata, overriding built-in defaults.

        :param metadata:
        """
        location = "/settings/node/metadata"
        data = self.call(
            "update_node_settings_metadata", location, method="PUT", body=metadata, schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def get_sheriff_complaint_groups_slice(
        self, after: int | None = None, before: int | None = None, limit: int | None = None,
        status: types.SheriffComplaintStatus | None = None
    ) -> types.SheriffComplaintGroupsSliceInfo:
        """
        Get a slice of the list of groups of complaints, optionally filtered by status, delimited by the ``before`` or
        ``after`` moment and the given ``limit``. If neither ``before`` nor ``after`` are provided, the latest groups
        are returned. The node may decide to return less groups than the given ``limit``. The groups are always sorted
        by moment, descending.

        :param after: filter groups created strongly after this moment
        :param before: filter groups created at or before this moment
        :param limit: maximum number of groups returned
        :param status: filter groups by status
        """
        location = "/sheriff/complaints/groups".format()
        params = {"after": after, "before": before, "limit": limit, "status": status}
        data = self.call(
            "get_sheriff_complaint_groups_slice", location, method="GET", auth=False, params=params,
            schema=schemas.SHERIFF_COMPLAINT_GROUPS_SLICE_INFO_SCHEMA
        )
        return types.SheriffComplaintGroupsSliceInfo.from_json(data)

    def get_sheriff_complaint_group(self, id: str) -> types.SheriffComplaintGroupInfo:
        """
        Get details of the given group of complaints.

        :param id: ID of the group of complaints
        """
        location = "/sheriff/complaints/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_sheriff_complaint_group", location, method="GET", auth=False,
            schema=schemas.SHERIFF_COMPLAINT_GROUP_INFO_SCHEMA
        )
        return types.SheriffComplaintGroupInfo.from_json(data)

    def get_sheriff_complaints_by_group(self, id: str) -> List[types.SheriffComplaintInfo]:
        """
        Get complaints included in the given group of complaints.

        :param id: ID of the group of complaints
        """
        location = "/sheriff/complaints/groups/{id}/complaints".format(id=quote_plus(id))
        data = self.call(
            "get_sheriff_complaints_by_group", location, method="GET", auth=False,
            schema=schemas.SHERIFF_COMPLAINT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SheriffComplaintInfo)

    def update_sheriff_complaint_group(
        self, id: str, decision: types.SheriffComplaintDecisionText
    ) -> types.SheriffComplaintGroupInfo:
        """
        Make a decision on the given group of complaints.

        :param id: ID of the group of complaints
        :param decision:
        """
        location = "/sheriff/complaints/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_sheriff_complaint_group", location, method="PUT", body=decision,
            schema=schemas.SHERIFF_COMPLAINT_GROUP_INFO_SCHEMA
        )
        return types.SheriffComplaintGroupInfo.from_json(data)

    def create_sheriff_complaint(self, complaint: types.SheriffComplaintText) -> types.SheriffComplaintInfo:
        """
        Send a complaint to the sheriff.

        :param complaint:
        """
        location = "/sheriff/complaints"
        data = self.call(
            "create_sheriff_complaint", location, method="POST", body=complaint,
            schema=schemas.SHERIFF_COMPLAINT_INFO_SCHEMA
        )
        return types.SheriffComplaintInfo.from_json(data)

    def create_sheriff_order(self, sheriff_order: types.SheriffOrderDetails) -> types.Result:
        """
        Receive and execute the sheriff's order.

        :param sheriff_order:
        """
        location = "/sheriff/orders"
        data = self.call(
            "create_sheriff_order", location, method="POST", body=sheriff_order, auth=False,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result.from_json(data)

    def get_story(self, id: str) -> types.StoryInfo:
        """
        Get an individual story.

        :param id: ID of the story
        """
        location = "/stories/{id}".format(id=quote_plus(id))
        data = self.call("get_story", location, method="GET", bodies=True, schema=schemas.STORY_INFO_SCHEMA)
        return types.StoryInfo.from_json(data)

    def update_story(self, id: str, story: types.StoryAttributes) -> types.StoryInfo:
        """
        Update the story.

        :param id: ID of the story
        :param story:
        """
        location = "/stories/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_story", location, method="PUT", body=story, bodies=True, schema=schemas.STORY_INFO_SCHEMA
        )
        return types.StoryInfo.from_json(data)

    def get_subscribers(
        self, node_name: str | None = None, type: types.SubscriptionType | None = None, feed_name: str | None = None,
        entry_id: str | None = None
    ) -> List[types.SubscriberInfo]:
        """
        Get the list of all subscribers, optionally filtered by some criteria.

        :param node_name: filter by subscribed node name
        :param type: filter by subscription type
        :param feed_name: filter by name of the feed subscribed to
        :param entry_id: filter by ID of the entry subscribed to
        """
        location = "/people/subscribers".format()
        params = {"nodeName": node_name, "type": type, "feedName": feed_name, "entryId": entry_id}
        data = self.call(
            "get_subscribers", location, method="GET", params=params, schema=schemas.SUBSCRIBER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriberInfo)

    def create_subscriber(self, subscriber: types.SubscriberDescription) -> types.SubscriberInfo:
        """
        Subscribe to a particular group of notifications.

        :param subscriber:
        """
        location = "/people/subscribers"
        data = self.call(
            "create_subscriber", location, method="POST", body=subscriber, schema=schemas.SUBSCRIBER_INFO_SCHEMA
        )
        return types.SubscriberInfo.from_json(data)

    def get_subscriber(self, id: str) -> types.SubscriberInfo:
        """
        Get an individual subscriber.

        :param id: ID of the subscriber
        """
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call("get_subscriber", location, method="GET", schema=schemas.SUBSCRIBER_INFO_SCHEMA)
        return types.SubscriberInfo.from_json(data)

    def update_subscriber(self, id: str, subscriber: types.SubscriberOverride) -> types.SubscriberInfo:
        """
        Update the subscriber's operations or set operations' overrides.

        :param id: ID of the subscriber
        :param subscriber:
        """
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_subscriber", location, method="PUT", body=subscriber, schema=schemas.SUBSCRIBER_INFO_SCHEMA
        )
        return types.SubscriberInfo.from_json(data)

    def delete_subscriber(self, id: str) -> types.ContactInfo:
        """
        Delete the subscriber and return the updated information about the node that was subscribed.

        :param id: ID of the subscriber
        """
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call("delete_subscriber", location, method="DELETE", schema=schemas.CONTACT_INFO_SCHEMA)
        return types.ContactInfo.from_json(data)

    def get_subscriptions(
        self, node_name: str | None = None, type: types.SubscriptionType | None = None
    ) -> List[types.SubscriptionInfo]:
        """
        Get the list of all subscriptions, optionally filtered by some criteria.

        :param node_name: filter by node name
        :param type: filter by subscription type
        """
        location = "/people/subscriptions".format()
        params = {"nodeName": node_name, "type": type}
        data = self.call(
            "get_subscriptions", location, method="GET", params=params, schema=schemas.SUBSCRIPTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriptionInfo)

    def create_subscription(self, subscription: types.SubscriptionDescription) -> types.SubscriptionInfo:
        """
        Register a subscription to notifications from a particular node.

        :param subscription:
        """
        location = "/people/subscriptions"
        data = self.call(
            "create_subscription", location, method="POST", body=subscription, schema=schemas.SUBSCRIPTION_INFO_SCHEMA
        )
        return types.SubscriptionInfo.from_json(data)

    def update_subscription(self, id: str, subscription: types.SubscriptionOverride) -> types.SubscriptionInfo:
        """
        Update the subscription's operations or set operations' overrides.

        :param id: ID of the subscription
        :param subscription:
        """
        location = "/people/subscriptions/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_subscription", location, method="PUT", body=subscription, schema=schemas.SUBSCRIPTION_INFO_SCHEMA
        )
        return types.SubscriptionInfo.from_json(data)

    def delete_subscription(self, id: str) -> types.ContactInfo:
        """
        Delete the subscription and return the updated information about the node that was subscribed to.

        :param id: ID of the subscription
        """
        location = "/people/subscriptions/{id}".format(id=quote_plus(id))
        data = self.call("delete_subscription", location, method="DELETE", schema=schemas.CONTACT_INFO_SCHEMA)
        return types.ContactInfo.from_json(data)

    def search_subscriptions(self, filter: types.SubscriptionFilter) -> List[types.SubscriptionInfo]:
        """
        Search for subscriptions by the given criteria.

        :param filter:
        """
        location = "/people/subscriptions/search"
        data = self.call(
            "search_subscriptions", location, method="POST", body=filter, schema=schemas.SUBSCRIPTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriptionInfo)

    def get_tokens(self) -> List[types.TokenInfo]:
        """
        Get the list of all existing tokens.
        """
        location = "/tokens"
        data = self.call("get_tokens", location, method="GET", schema=schemas.TOKEN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.TokenInfo)

    def create_token(self, token: types.TokenAttributes) -> types.TokenInfo:
        """
        Sign in and create a token.

        :param token:
        """
        location = "/tokens"
        data = self.call(
            "create_token", location, method="POST", body=token, auth=False, schema=schemas.TOKEN_INFO_SCHEMA
        )
        return types.TokenInfo.from_json(data)

    def get_token_info(self, id: str) -> types.TokenInfo:
        """
        Get information about the token.

        :param id: ID of the token
        """
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("get_token_info", location, method="GET", schema=schemas.TOKEN_INFO_SCHEMA)
        return types.TokenInfo.from_json(data)

    def update_token(self, id: str, token: types.TokenName) -> types.TokenInfo:
        """
        Update the name of the token.

        :param id: ID of the token
        :param token:
        """
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("update_token", location, method="PUT", body=token, schema=schemas.TOKEN_INFO_SCHEMA)
        return types.TokenInfo.from_json(data)

    def delete_token(self, id: str) -> types.Result:
        """
        Delete the token.

        :param id: ID of the token
        """
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("delete_token", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def get_user_list_general(self, name: str) -> types.UserListInfo:
        """
        Get the general information about the user list given.

        :param name: the name of the list
        """
        location = "/user-lists/{name}".format(name=quote_plus(name))
        data = self.call(
            "get_user_list_general", location, method="GET", auth=False, schema=schemas.USER_LIST_INFO_SCHEMA
        )
        return types.UserListInfo.from_json(data)

    def get_user_list_slice(
        self, name: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.UserListSliceInfo:
        """
        Get a slice of the user list, delimited by the ``before`` or ``after`` moment and the given ``limit``. If
        neither ``before`` nor ``after`` are provided, the latest items are returned. The node may decide to return
        fewer items than the given ``limit``. The items are always sorted by moment, descending.

        :param name: the name of the list
        :param after: filter items created strongly after this moment
        :param before: filter items created at or before this moment
        :param limit: maximum number of items returned
        """
        location = "/user-lists/{name}/items".format(name=quote_plus(name))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_user_list_slice", location, method="GET", auth=False, params=params,
            schema=schemas.USER_LIST_SLICE_INFO_SCHEMA
        )
        return types.UserListSliceInfo.from_json(data)

    def get_user_list_item(self, name: str, node_name: str) -> types.UserListItemInfo:
        """
        Get the information from the user list about the node given.

        :param name: the name of the list
        :param node_name: the node name to get information about
        """
        location = "/user-lists/{name}/items/{nodeName}".format(name=quote_plus(name), nodeName=quote_plus(node_name))
        data = self.call(
            "get_user_list_item", location, method="GET", auth=False, schema=schemas.USER_LIST_ITEM_INFO_SCHEMA
        )
        return types.UserListItemInfo.from_json(data)

    def create_user_list_item(self, name: str, item: types.UserListItemAttributes) -> types.UserListItemInfo:
        """
        Add a node to the user list.

        :param name: the name of the list
        :param item:
        """
        location = "/user-lists/{name}/items".format(name=quote_plus(name))
        data = self.call(
            "create_user_list_item", location, method="POST", body=item, schema=schemas.USER_LIST_ITEM_INFO_SCHEMA
        )
        return types.UserListItemInfo.from_json(data)

    def delete_user_list_item(self, name: str, node_name: str) -> types.Result:
        """
        Delete a node from the user list

        :param name: the name of the list
        :param node_name: the node name to delete
        """
        location = "/user-lists/{name}/items/{nodeName}".format(name=quote_plus(name), nodeName=quote_plus(node_name))
        data = self.call("delete_user_list_item", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result.from_json(data)

    def who_am_i(self) -> types.WhoAmI:
        """
        Get brief information about the node.
        """
        location = "/whoami"
        data = self.call("who_am_i", location, method="GET", auth=False, schema=schemas.WHO_AM_I_SCHEMA)
        return types.WhoAmI.from_json(data)
