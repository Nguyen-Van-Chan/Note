### cài đặt theo hướng dẫn tại 
https://facebook.github.io/react-native/docs/getting-started

The issue is closed but in case if above answers don't work.
put this in console -> xcrun -k --sdk iphoneos --show-sdk-path
if the answer is
xcrun:_ error: SDK "iphoneos" cannot be located
xcrun: error: SDK "iphoneos" cannot be located
xcrun: error: unable to lookup item 'Path' in SDK 'iphoneos'

then put this sudo xcode-select --switch /Applications/Xcode.app

Then install pod again

sudo npm install --global --unsafe-perm ios-deploy
