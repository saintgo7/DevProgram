// Line Trace
// Program 087

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program087.generated.h"

UCLASS()
class AProgram087 : public AActor
{
    GENERATED_BODY()

public:
    AProgram087();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
