# Image optimization script for Angaza-Tumaini
# Usage: run in PowerShell from repository root (ensure you have ImageMagick "magick" or cwebp installed)

$images = @('6-29','6-27','6-28','6-16','6-2','6-13','6-22','6-32','Joram')
$sizes = @(1600,1200,800)

# Helper: check for a command
function Has-Command($name) {
    $which = (Get-Command $name -ErrorAction SilentlyContinue)
    return $which -ne $null
}

if (Has-Command 'magick') {
    Write-Output "ImageMagick detected (magick). Generating resized JPGs and WebP files..."
    foreach ($img in $images) {
        $src = "filez/$img.jpg"
        if (Test-Path $src) {
            foreach ($w in $sizes) {
                $outJpg = "filez/$img-$w.jpg"
                Write-Output "Creating $outJpg"
                magick "${src}" -resize ${w}x -quality 82 "${outJpg}"
                $outWebp = "filez/$img-$w.webp"
                Write-Output "Creating $outWebp"
                magick "${outJpg}" -quality 80 "${outWebp}"
            }
        } else {
            Write-Output "Missing source: $src"
        }
    }
    Write-Output "Done. Review the files under filez/ and commit as needed."

} elseif (Has-Command 'cwebp') {
    Write-Output "cwebp detected but ImageMagick not found. Creating resized JPGs requires ImageMagick."
    Write-Output "If you have ImageMagick, install it and re-run this script. Alternatively, create resized JPGs by hand then run cwebp conversions."

    foreach ($img in $images) {
        foreach ($w in $sizes) {
            $in = "filez/${img}-${w}.jpg"
            if (Test-Path $in) {
                $outWebp = "filez/${img}-${w}.webp"
                Write-Output "Converting $in -> $outWebp"
                cwebp -q 80 "${in}" -o "${outWebp}"
            } else {
                Write-Output "Missing resized jpg: $in"
            }
        }
    }
    Write-Output "Done (cwebp path)."

} else {
    Write-Output "Neither ImageMagick (magick) nor cwebp were found on PATH."
    Write-Output "Please install ImageMagick (https://imagemagick.org) or Google cwebp (part of libwebp) and re-run this script."
    Write-Output "Alternatively, you can convert with a GUI image tool and place files like filez/6-29-1200.jpg and filez/6-29-1200.webp before running this script." 
}
