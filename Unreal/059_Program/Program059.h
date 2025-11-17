// Sublevel
// Program 059

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program059.generated.h"

UCLASS()
class AProgram059 : public AActor
{
    GENERATED_BODY()

public:
    AProgram059();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
