# crond-lambda
# 
# Created and modified using https://aws.amazon.com/blogs/compute/scheduling-ssh-jobs-using-aws-lambda/
# 
A simple crond implementation on AWS lambda


This script gets the private IP of the first matching AWS instance that matches the "SERVERNAME" argument provided. SSH's in and runs the cmd(s) passed to the function. 

Example Input

```
{
  "SERVERNAME": "server-1",
  "CMD": "php /root/script_to_execute.php"
}
```

Can be deployed using https://github.com/nficano/python-lambda or manually.

