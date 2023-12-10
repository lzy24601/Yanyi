def get_resnet_arch(model_type, opt, in_channels=3):
    setup = model_type.split("_")[1]

    if setup == "256W8UpDown":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                64,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                128,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                3,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W5UpDown64":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                opt.ngf,
                64,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                3,
            ],
            "upsample": [
                "Down",
                "Down",
                False,
                "Up",
                "Up",
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }
    elif setup == "256W8UpDown64":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                64,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                3,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }
    elif setup == "256W16UpDown64":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                64,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                3,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W8UpDown64BG":
        arch = {
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                3,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                3,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W5UpDown64BG":
        arch = {
            "downsample": [
                False,
                False,
                False,
            ],
            "layers_dec": [
                3,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf,
                3,
            ],
            "upsample": [
                "Down",
                "Down",
                False,
                "Up",
                "Up",
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W8UpDown64Alpha":
        arch = {
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                3,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                2,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W8UpDown64SingleAlpha":
        arch = {
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                3,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                1,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W8UpDown64Layers":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                opt.ngf,
                opt.out_channel,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64+opt.addtional_decoder_input,
                opt.ngf,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                opt.ngf * 2,
                opt.ngf * 2,
                3+opt.addtional_decoder_output,
            ],
            "upsample": [
                False,
                "Down",
                "Down",
                False,
                "Up",
                "Up",
                False,
                False,
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }


    elif setup == "256W5UpDown64Layers":
        arch = {
            "downsample": [
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 4,
                opt.ngf * 2,
                3+opt.addtional_decoder_output,
            ],
            "upsample": [
                "Down",
                "Down",
                False,
                "Up",
                "Up",
            ],
            "activation": [
                "Relu",
                "Relu",
                "Relu",
                "Relu",
                "Relu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    elif setup == "256W4UpDown64Motion":
        arch = {
            "layers_enc": [
                in_channels,
                opt.ngf // 2,
                opt.ngf // 2,
                opt.ngf,
                64,
            ],
            "downsample": [
                False,
                False,
                False,
                False,
            ],
            "layers_dec": [
                64,
                opt.ngf * 2,
                opt.ngf * 4,
                opt.ngf * 2,
                2,
            ],
            "upsample": [
                "Down",
                False,
                "Up",
                False,
            ],
            "activation": [
                "LRelu",
                "LRelu",
                "LRelu",
                "LRelu",
            ],
            "non_local": False,
            "non_local_index": 1,
        }

    return arch
