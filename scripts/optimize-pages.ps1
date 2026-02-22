# Generate resized JPGs and WebP files for specified images
$sizes = @(1600,1200,800)
$targets = @('filez/Programs.jpg','filez/Impact.jpg')
if (-not (Get-Command magick -ErrorAction SilentlyContinue)) {
    Write-Error "ImageMagick 'magick' not found on PATH. Install ImageMagick and re-run this script."
    exit 1
}
foreach ($t in $targets) {
    if (Test-Path $t) {
        $base = [System.IO.Path]::GetFileNameWithoutExtension($t)
        foreach ($w in $sizes) {
            $outJpg = "filez/$base-$w.jpg"
            Write-Output "Creating $outJpg"
            magick $t -resize ${w}x -quality 82 $outJpg
            $outWebp = "filez/$base-$w.webp"
            Write-Output "Creating $outWebp"
            magick $outJpg -quality 80 $outWebp
        }
    } else {
        Write-Output "Missing source: $t"
    }
}
Write-Output "Pages optimization complete."
