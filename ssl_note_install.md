# How to Setting Up a Comodo SSL Cert

* I advice you to buy SSL Certs from officially Comodo only , or some SSL reseller whose you trust.

These are the steps I went through to set up an SSL cert.
Purchase the cert

Prior to purchasing a cert, you need to generate a private key, and a CSR file (Certificate Signing Request). You’ll be asked for the content of the CSR file when ordering the certificate:

	openssl req -new -newkey rsa:2048 -nodes -keyout example_com.key -out example_com.csr

This gives you two files:

    example_com.key — your Private key. You’ll need this later to configure ngxinx.
    example_com.csr — Your CSR file.

Now, purchase the certificate , follow the steps on their site, and you should soon get an email with your PositiveSSL Certificate. It contains a zip file with the following:

    Root CA Certificate – AddTrustExternalCARoot.crt
    Intermediate CA Certificate – COMODORSAAddTrustCA.crt
    Intermediate CA Certificate – COMODORSADomainValidationSecureServerCA.crt
    Your PositiveSSL Certificate – www_example_com.crt (or the subdomain you gave them)

Install the Commodo SSL cert

Combine everything for nginx:

Combine the above crt files into a bundle (the order matters, here):

```bash
    cat www_example_com.crt COMODORSADomainValidationSecureServerCA.crt  COMODORSAAddTrustCA.crt AddTrustExternalCARoot.crt > ssl-bundle.crt
```

Store the bundle wherever nginx expects to find it:

```bash
    mkdir -p /etc/nginx/ssl/example_com/
    mv ssl-bundle.crt /etc/nginx/ssl/example_com/
```

Ensure your private key is somewhere nginx can read it, as well.:

```bash
    mv example_com.key /etc/nginx/ssl/example_com/
```

Make sure your nginx config points to the right cert file and to the private key you generated earlier:


```nginx
    server {
        listen 443;

        ssl on;
        ssl_certificate /etc/nginx/ssl/example_com/ssl-bundle.crt;
        ssl_certificate_key /etc/nginx/ssl/example_com/example_com.key;

        # side note: only use TLS since SSLv2 and SSLv3 have had recent vulnerabilities
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;

        # ...

    }

```

Restart nginx.

For *CA Bundle* you need below steps.

For Comodo PositiveSSL CA certificates these are: *AddTrustExternalCARoot.crt*, *COMODORSAAddTrustCA.crt* and *COMODORSADomainValidationSecureServerCA.crt*

To combine them, run the following command in terminal:

	$ cat COMODORSADomainValidationSecureServerCA.crt COMODORSAAddTrustCA.crt AddTrustExternalCARoot.crt >> bundle.crt

If you have new version of Certificate use Below Documentation.


# 2019 Comodo Certificates


In case of Comodo certificates, you should receive the zip archive with *.crt and .ca-bundle files. Geotrust/Thawte/Symantec sends certificates in plain text. Simply save the certificates as txt files. Notepad will meet this demand. For Comodo PositiveSSL the files would appear like the ones below:

* **yourdomainname.crt**
* **yourdomainname.ca-bundle**

or you may receive the CA bundle in separate files as provided below:

* **SectigoRSADomainValidationSecureServerCA.crt**

* **USERTrustRSAAddTrustCA.crt**

* **AddTrustExternalCARoot.crt**

Combine CA certificates in the single file.

If you received several CA certificates in separate files, you should combine them in the single file to make the CA bundle. You can also download a completed Bundle file here .

For Comodo PositiveSSL CA certificates in 2019 these are: *AddTrustExternalCARoot.crt*, *USERTrustRSAAddTrustCA.crt* and *SectigoRSADomainValidationSecureServerCA.crt*

To combine them, run the following command in terminal:

```bash
$ cat SectigoRSADomainValidationSecureServerCA.crt USERTrustRSAAddTrustCA.crt AddTrustExternalCARoot.crt >> CA_bundle.crt
```

For **Nginx**

```bash
$ cat www_example_com.crt SectigoRSADomainValidationSecureServerCA.crt USERTrustRSAAddTrustCA.crt AddTrustExternalCARoot.crt >> ssl_bundle.crt
```

# How do I verify that a private key matches a certificate? (OpenSSL)

How do I verify that a private key matches a certificate?

To verify that a private key matches its certificate you need to compare the modulus of the certificate against the modulus of the private key.

Please follow the below command to view the modulus of the certificate.
```bash
openssl x509 -noout -modulus -in server.crt | openssl md5
```
Now you will receive the modulus something like a77c7953ea5283056a0c9ad75b274b96

Please follow the below command to view the modulus of the private key.
```bash
openssl rsa -noout -modulus -in myserver.key | openssl md5
```
Now you should get the modulus as same as certificate modulus above. i.e a77c7953ea5283056a0c9ad75b274b96

For CA bundle run below command

```bash
openssl verify -CAfile CA_bundle.crt www_example_com.crt
```

# How to Convert .pem to .cert with OpenSSL

```bash
openssl x509 -outform der -in your-cert.pem -out your-cert.crt
````

# How to Create .pem file including Certificate and Private Key

* How to create a self-signed PEM file:

```bash
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```


* How to create a PEM filefrom existing certificate files that form a chain:

(optional) Remove the password from the Private Key by following the steps listed below:

```bash
openssl rsa -in server.key -out nopassword.key
```
Note: Enter the pass phrase of the Private Key.

* Combine the private key, public certificate and any 3rd party intermediate certificate files:

```bash
cat nopassword.key > server.pem
cat server.crt >> server.pem

Note: Repeat this step as needed for third-party certificate chain files, bundles, etc:

cat intermediate.crt >> server.pem
```
* Always remember First Key => Cert => Intermediate

# How to create a PFX file from existing certificate files and key.

```
openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile more.crt
```
Breaking down the command:

```
openssl – the command for executing OpenSSL
pkcs12 – the file utility for PKCS#12 files in OpenSSL
  -export -out certificate.pfx – export and save the PFX file as certificate.pfx
  -inkey privateKey.key – use the private key file privateKey.key as the private key to combine with the certificate.
  -in certificate.crt – use certificate.crt as the certificate the private key will be combined with.
  -certfile more.crt – This is optional, this is if you have any additional certificates you would like to include in the PFX file.
```

Note: After entering the command, you will be prompted to enter and verify an export password to protect the PFX file. Remember this password! You will need it when you wish to export the certificates and key.
