# Load with: source pyPORIS/scripts/poris-completion.bash
# Model paths are relative to models/ in the current working directory,
# matching porispanel.sh. No bash-completion package is required.
_poris_model_complete() {
    local current="${COMP_WORDS[COMP_CWORD]}"
    local previous="${COMP_WORDS[COMP_CWORD-1]}"
    local path candidate option
    local directories_only=0
    COMPREPLY=()
    [[ $previous == --cluster ]] && return 0
    case "${COMP_WORDS[0]##*/}" in
        porispanel_dir.sh|porispanel_dir_csys.sh) directories_only=1 ;;
    esac
    for option in "${COMP_WORDS[@]:1:COMP_CWORD-1}"; do
        [[ $option == --dir ]] && directories_only=1
    done
    if [[ $current == --* ]]; then
        while IFS= read -r option; do
            COMPREPLY+=("$option")
        done < <(compgen -W '--dir --csys --ods --parser-xml --compare-parser --debug --web --no-panel --cluster' -- "$current")
        return 0
    fi
    while IFS= read -r path; do
        candidate=${path#models/}
        if [[ -d $path ]]; then
            COMPREPLY+=("${candidate}/")
        elif [[ $directories_only == 0 && $path == *.graphml ]]; then
            COMPREPLY+=("${candidate%.graphml}")
        fi
    done < <(compgen -f -- "models/$current")
    # Keep Tab traversal inside directories; final model names get a space.
    compopt -o filenames 2>/dev/null || :
    if [[ ${#COMPREPLY[@]} == 1 && ${COMPREPLY[0]} == */ ]]; then
        compopt -o nospace 2>/dev/null || :
    fi
    return 0
}

complete -F _poris_model_complete porispanel.sh porispanel_csys.sh \
    porispanel_dir.sh porispanel_dir_csys.sh
