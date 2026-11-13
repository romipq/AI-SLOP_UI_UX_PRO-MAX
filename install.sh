#!/usr/bin/env bash
# install.sh — register AI-SLOP UI/UX PRO-MAX with Claude Code (or any skills folder).
#
#   ./install.sh                     symlink into ~/.claude/skills
#   ./install.sh --copy              copy instead of symlink
#   ./install.sh --target DIR        custom skills directory
#   ./install.sh --uninstall         remove the installed skill
#   ./install.sh --force             replace an existing install
#
# MIT © 2026 romipq

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="ai-slop-ui-ux-pro-max"
TARGET_DIR="${HOME}/.claude/skills"
MODE="link"
UNINSTALL=0
FORCE=0

usage() {
  sed -n '2,12p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy) MODE="copy" ;;
    --target) shift; TARGET_DIR="${1:?--target needs a directory}" ;;
    --target=*) TARGET_DIR="${1#*=}" ;;
    --uninstall) UNINSTALL=1 ;;
    --force) FORCE=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown option: $1" >&2; usage; exit 2 ;;
  esac
  shift
done

DEST="${TARGET_DIR}/${SKILL_NAME}"

if [[ "${UNINSTALL}" -eq 1 ]]; then
  if [[ -e "${DEST}" || -L "${DEST}" ]]; then
    rm -rf "${DEST}"
    echo "removed ${DEST}"
  else
    echo "nothing to remove at ${DEST}"
  fi
  exit 0
fi

if [[ ! -f "${SCRIPT_DIR}/SKILL.md" ]]; then
  echo "error: SKILL.md not found — run this script from the repository root" >&2
  exit 1
fi

if [[ -e "${DEST}" || -L "${DEST}" ]]; then
  if [[ "${FORCE}" -ne 1 ]]; then
    echo "error: ${DEST} already exists (use --force to replace)" >&2
    exit 1
  fi
  rm -rf "${DEST}"
fi

mkdir -p "${TARGET_DIR}"

if [[ "${MODE}" == "copy" ]]; then
  cp -R "${SCRIPT_DIR}" "${DEST}"
  echo "copied  ${SCRIPT_DIR} → ${DEST}"
else
  ln -s "${SCRIPT_DIR}" "${DEST}"
  echo "linked  ${SCRIPT_DIR} → ${DEST}"
fi

cat <<EOF

✨ Installed ${SKILL_NAME}

  entry   ${DEST}/SKILL.md
  verify  python3 "${SCRIPT_DIR}/tools/slop_lint.py" "${SCRIPT_DIR}/examples/01-max-landing.html"

Next:
  • Claude Code: run /skills and look for "${SKILL_NAME}"
  • Other agents: see docs/INSTALL.md

EOF
