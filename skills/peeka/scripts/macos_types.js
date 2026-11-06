// Read-only JXA bridge. Run through osascript; input is a JSON argument, not code.
ObjC.import('Foundation');
ObjC.import('CoreServices');

function run(argv) {
    const request = JSON.parse(argv[0]);
    const url = $.NSURL.fileURLWithPath(request.path);
    function resource(key) {
        const value = Ref();
        const error = Ref();
        if (!url.getResourceValueForKeyError(value, key, error)) return null;
        return ObjC.unwrap(value[0]);
    }
    const type = resource($.NSURLTypeIdentifierKey);
    const ubiquitous = resource($.NSURLIsUbiquitousItemKey);
    const downloadStatus = resource($.NSURLUbiquitousItemDownloadingStatusKey);
    const downloaded = resource($.NSURLUbiquitousItemIsDownloadedKey);
    const matches = [];
    if (type) {
        for (const candidate of request.types || []) {
            // C functions require bridged NSString arguments, not JS strings.
            if (type === candidate || $.UTTypeConformsTo($(type), $(candidate))) {
                matches.push(candidate);
            }
        }
    }
    return JSON.stringify({
        uti: type,
        conforming_types: matches,
        ubiquitous: ubiquitous,
        download_status: downloadStatus,
        downloaded: downloaded
    });
}
