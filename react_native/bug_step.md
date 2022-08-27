# create project 
``
npx react-native init AwesomeProject
``

## font icon bug
dd in App.js
```
import Icon from 'react-native-vector-icons/MaterialIcons'

Icon.loadFont();
```
In your case you have to import the font awesome
