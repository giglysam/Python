from pytube import YouTube
link = input('Enter the link: ')


def repeat():
    knil = input('Enter info: ')
    yt = YouTube(link)
    if knil.__contains__("title"):
        print('Title: ', yt.title)
    elif knil.__contains__("views"):
        print('Number of views: ', yt.views)
    elif knil.__contains__("thumbnail_url"):
        print('thumbnail_url: ', yt.thumbnail_url)
    elif knil.__contains__("rating"):
        print('rating: ', yt.rating)
    elif knil.__contains__("length"):
        print('length: ', yt.length)
    elif knil.__contains__("author"):
        print('author: ', yt.author)
    elif knil.__contains__("description"):
        print('description: ', yt.description)
    elif knil.__contains__("publish_date"):
        print('publish_date: ', yt.publish_date)
    elif knil.__contains__("vid_info"):
        print('vid_info: ', yt.vid_info)
    elif knil.__contains__("age_restricted"):
        print('age_restricted: ', yt.age_restricted)
    elif knil.__contains__("exit"):
        quit()

    else:
        repeat()


repeat()