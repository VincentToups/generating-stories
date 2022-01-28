import web_util as w;
import sys, argparse

root = "https://teddit.net"

def grab_page(page_url):
    bs = w.get_bs(page_url);
    post_body = bs.find("div",class_="usertext-body").text;
    title = bs.find("div",class_="title").find("a").text
    flair = [];
    for el in bs.find("div",class_="title").find_all("span",class_="flair"):
        flair = flair + [el.text];
    return "::: " + title + " (" + ", ".join(flair) + ")" + " :::\n" + post_body;

lead = '/r/AmItheAsshole/comments'
def just_aita_links(bs):
    anchors = bs.find_all("a");
    def keeper(anchor):
        return (anchor.has_attr('href') and len(anchor["href"]) >= len(lead) and (anchor["href"][0:len(lead)] == lead))
    return [root + a['href'] for a in anchors if keeper(a)];

def next_link(bs):
    candidates = bs.find_all("a");
    for cand in candidates:
        if cand.text.strip() == 'next ›':
            return root + cand['href'];
    return None;

def grab_top_links(start_url, pages, output = []):
    page = 0;
    bs = w.get_bs(start_url);
    done = False;
    while not done and page < pages:
        story_links = just_aita_links(bs);
        print("{} stories on page {}".format(len(story_links), page));
        output.extend(story_links);
        nl = next_link(bs);
        if nl:
            bs = w.get_bs(next_link(bs));
        else:
            done = True;
        page = page + 1;
    return list(set(output));

def grab_page_data(links, output_file):
    i = 0;
    with open(output_file,"w") as f:
        for l in links:
            try:
                data = grab_page(l);
                f.write(data);
                f.write("\n");
                print("{}".format(i));
                i = i + 1;
            except:
                print("Error for {}".format(l));
    print("Done!");

#grab_page_data(grab_top_links("https://teddit.net/r/AmItheAsshole/top?t=all", 50), "aita.txt")

def main(args):
    grab_page_data(grab_top_links("https://teddit.net/r/{}/top?t=all".format(args.subreddit), args.n_pages), args.output)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output');
    parser.add_argument('-s', '--subreddit');
    parser.add_argument('-n', '--n_pages', type=int, default=50);
    args = parser.parse_args()
    lead = '/r/{}/comments'.format(args.subreddit)
    main(args)
