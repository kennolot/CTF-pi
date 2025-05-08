## CTF-pi - Fluentbit - Difficulty: ★★☆☆☆

### Scenario

My IoT systems got too complex so I had to come up with a better logging solution to not get overwhelmed as my system scales up, luckily for me I found a general purpose log processor fluentbit. 

I played around with it a bit, but I didn't understanda thing, that was a year ago. I don't think I deleted it afterwards.

### Prerequisites

Especially for Pi 5 you'll have to temporarily add this to `/boot/firmware/config.txt`

```
# temporarily enable 4K PAGESIZE
kernel=kernel8.img
```

If you get memory errors on other models make sure you are using 4K pagesize. The problem with 16K which should be default on Pi 5 is that it's not supported by a-lot of software, so your application will crash right away or keep restarting due to memory errors.

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi6_2` directory.

`docker compose` works.

### Objective

From the scenario we can assume the version is outdated, find what version is being used and what CVEs exist for it. 

Even though Remote code execution and thus root access could  be gained with the exploit, the challenge can also be marked as completed when the fluentbit service is crashed (denial of service).

### **Hints**

<details>
<summary>Click me</summary>

https://www.vicarius.io/vsociety/posts/linguistic-lumberjack-memory-corruption-in-fluent-bit-cve-2024-4323

</details>

### Cleaning up

To revert the PAGESIZE change just delete these lines in `/boot/firmware/config.txt` and reboot.
```
# temporarily enable 4K PAGESIZE
kernel=kernel8.img
```

Though it might be better to just keep it, the performance boost from 16K pagesize only comes noticable with high workloads. https://github.com/raspiblitz/raspiblitz/issues/4346

Also run `docker compose down` to stop the container.
