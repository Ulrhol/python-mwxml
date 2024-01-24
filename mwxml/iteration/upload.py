import mwtypes

from ..errors import MalformedXML
from .user import User

class Upload(mwtypes.Upload):
    """
    Upload metadata and content.  See :class:`mwtypes.Upload` for a
    description of fields.
    """

    @classmethod
    def from_element(cls, element):

        id = None
        timestamp = None
        filename = None
        comment = None
        content = None
        size = None
        source = None

        for sub_element in element:
            tag = sub_element.tag
            if tag == "id":
                id = int(sub_element.text)
            elif tag == "timestamp":
                timestamp = mwtypes.Timestamp(sub_element.text)
            elif tag == "contributor":
                user_deleted = sub_element.attr('deleted') is not None
                if not user_deleted:
                    user = User.from_element(sub_element)
            elif tag == "sha1":
                sha1 = sub_element.text
            elif tag == "filename":
                filename = sub_element.text
            elif tag == "size":
                size = sub_element.text
            elif tag == "comment":
                 comment = sub_element.text
            elif tag == "src":
                source = sub_element.text
            elif tag == "contents":
                content = sub_element.text
            elif tag == "rel":
                rel = sub_element.text
            elif tag == "sha1base36":
                sha1 = sub_element.text
            elif tag == "archivename":
                archivename = sub_element.text
            else:
                raise MalformedXML("Unexpected tag found when processing " +
                                   "a <revision>: '{0}'".format(tag))

        return cls(
            id, timestamp,
            filename=filename,
            comment=comment,
            content=content,
            size=size
        )
