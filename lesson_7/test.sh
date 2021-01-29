ZERO=test.py
echo initial: $ZERO

FIRST=$ZERO
SECOND=`python3 $FIRST`

while [ "$SECOND" != "$ZERO" ]
do
    cp $FIRST $SECOND
    echo copied: $SECOND
    
    FIRST=$SECOND
    SECOND=`python3 $FIRST`
done
