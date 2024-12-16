#!/usr/bin/node
exports.callMeMobby = function (x, thefunction) {
    for (let i = 0; i < x; i++) {
        thefunction();
    }
}
