# crond-lambda
A simple crond implementation on AWS lambda


This script gets the private IP of the first matching AWS instance that matches the "SERVERNAME" argument provided. SSH's in and runs the cmd(s) passed to the function. 

Example Input

```
{
  "SERVERNAME": "server-1",
  "CMD": "php /root/script_to_execute.php"
}
```
