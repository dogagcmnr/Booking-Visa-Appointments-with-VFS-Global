# VFSGlobal Appointment Checker
Regularly checks for visa appointments in specific visa centres on VFS Global Online Portal.

## Usage
- Add your account details through 'password.py' file.
```
userid='your-email-goes-here'
pw='your-password-goes-here'
```
- Start the program and enter the captcha manually.
- Click login.

## Different Centres
- Please find these lines 25 and 27 in 'start.py' file.
```
selelement.select_by_visible_text('Poland Visa Application Center - Ankara')
```

```
selelement.select_by_visible_text('Poland Visa Application Center-Altunizade')
```
- Change the lines or duplicate according to your visa centre preference.

## Good luck!
