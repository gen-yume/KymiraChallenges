# Kymira Challenges
## Overview
This repository contains the challenges used to evaluate AI agents from within
Kymira. The repository is laid out using the following structure:
```
.
├── easy
│   ├── challengeA1
│   └── challengeA2
├── medium
│   ├── challengeB1
│   └── challengeB2
├── hard
│   ├── challengeC1
│   └── challengeC2
├── insane
│   ├── challengeD1
│   └── challengeD2
└── sota
    ├── challengeE1
    └── challengeE2
```

## Difficulty Levels
Each challenge difficulty level is designed to target a specific class of LLM
models, plus an approximate workload implementation complexity. The current
guidelines for the difficulty levels are as follows:

* Easy
  * LLM size: Small (capable of running locally on 8-16GB of VRAM)
  * Workload complexity: Low
* Medium
  * LLM size: Medium (capable of running locally on high VRAM GPUs)
  * Workload complexity: Medium
* High
  * LLM size: Large (cloud-only)
  * Workload complexity: Medium
* Insane
  * LLM size: Large (cloud-only)
  * Workload complexity: High
* State of the Art (SotA)
  * LLM size: Large (cloud-only)
  * Workload complexity: High

The goals for each tier are as follows:

* Easy
  * Basic challenges that primarily act as a sanity test for assistant and/or
    workload implementations
  * Should be possible to complete with a small LLM and little guidance from
    a workload
* Medium
  * More difficult challenges that are not easily/consistently solved by small
    LLMs
  * Will generally require either a larger LLM with a minimal complexity
    workload, or a small LLM with heavy guidance from a workload
* High
  * Complex challenges that generally require cloud-based LLMs
* Insane
  * Highly complex challenges that require both a powerful, cloud-based LLM
    and a complex workload capable of guiding the LLM through the task
* SOTA
  * Challenges that push the boundaries of what's possible to complete using
    LLMs

Each challenge is provided as a self-contained folder. Each folder provides
a docker-compose file, allowing Kymira to set up a container and run the
workload within the container when evaluating an assistant+workload implementation.

## Job Specs
Kymira requires that each job be defined using a YAML-based specification so
that Kymira executors understand how to handle the job. These specifications
are normally provided via the Kymira UI, but are also defined within this
repository as `job.yml` files in each challenge's folder for demonstration
purposes. An `example-job-spec.yml` file is also present in the root folder
of this repository, which contains a highly commented version of the `two-sum`
challenge's `job.yml` file.
