let data = [{keyword: 'coffee', tip: 'this is a tip'}, {keyword: 'can', tip: 'this is a tip'}];

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	if (changeInfo.title) {
		let googleSearch = (changeInfo.title).split(" ");
		let search = "";
		let tipIndices = [];
		let size = googleSearch.length;
		if (googleSearch[size-2] == "Google" && googleSearch[size-1] == "Search") {
			googleSearch.pop();
			googleSearch.pop();
			googleSearch.pop();
			search = googleSearch.join(" ");

			data.forEach((object, i) => {
				if (search.includes(object.keyword)) {
					tipIndices.push(i);
				}
			});
			desktopNotification(tipIndices);
		}
	}
});

function desktopNotification(tipIndices) {
	var opt = {
  		type: "basic",
  		title: "Eco Friendly Tip!",
  		message: "tip",
  		iconUrl: "./icon128.png"
	}

	tipIndices.forEach((index) => {
		opt.message = data[index].tip;
		chrome.notifications.create("", opt, () => {});
	})
}