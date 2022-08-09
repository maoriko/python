terraform () {
	local ARGS=() ENVIRONMENT=()
	local EXTRA ENVS KEY VAL CHDIR EXTRA_ARGS LOCAL_ARGS=("$@")
	if [[ ! "$PWD" =~ ${HOME} ]]
	then
		echo -e "\033[0;31mThis function can be used only from a folder that is part of the user home dir"
		[[ $(type "$(where terraform | tail -1)") =~ "bash function" ]] && echo -e "install terraform and use it\033[0m" || echo -e "Use $(where terraform | tail -1) insted of terraform\033[0m"
		return 1
	fi
	ENVS=($(env | grep TF_))
	for ENV in "${ENVS[@]}"
	do
		KEY=$(cut -d= -f1 <<<"${ENV}")
		VAL=$(cut -d= -f2 <<<"${ENV}")
		if [[ $KEY =~ (PATH|FILE) ]]
		then
			mkdir -p "${VAL%/*}"
			[[ $VAL =~ ${HOME} ]] && VAL="${VAL//$HOME//workspace}"  || VAL="${PWD/#$HOME\//}/${VAL}"
		fi
		ENVIRONMENT+=("-e ${KEY}=${VAL}")
	done
	# shellcheck disable=SC2199
	if [[ "${LOCAL_ARGS[@]}" =~ -chdir ]]
	then
		PDIR=$(echo "${LOCAL_ARGS[@]}" | grep -Eo 'chdir=.*' | cut -d' ' -f1 | cut -d = -f2)
		[[ "${PDIR}" =~ $HOME ]] && CHDIR="${PDIR//$HOME//workspace}"  || CHDIR="${PDIR/#$HOME\//}/${PDIR}"
		ARGS+=("-chdir=${CHDIR}")
	else
		[[ "${PWD}" != "${HOME}" ]] && ARGS+=("-chdir=${PWD/#$HOME\//}")
	fi
	# shellcheck disable=SC2199
	if [[ "${LOCAL_ARGS[@]}" =~ console ]]
	then
		EXTRA='-it'
	elif [[ "${LOCAL_ARGS[@]}" =~ autocomplete ]]
	then
		command terraform "${LOCAL_ARGS[@]}"
		return
	else
		EXTRA='-i'
	fi
	EXTRA_ARGS=(${LOCAL_ARGS[@]/"-chdir=${PDIR}"})
	[[ "$(get_digest  "hashicorp/terraform")" != "$(get_remote_digest  "hashicorp/terraform" "latest")" ]] && docker pull hashicorp/terraform:latest
	command docker run --platform linux/amd64 --rm -u "$(id -u)" ${EXTRA} -e "HOME=/workspace" $(echo ${ENVIRONMENT[*]}) -v "${HOME}:/workspace" -w /workspace hashicorp/terraform $(echo ${ARGS[*]}) $(echo ${EXTRA_ARGS[*]})
}