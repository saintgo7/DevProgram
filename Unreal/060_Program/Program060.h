// World Composition
// Program 060

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program060.generated.h"

UCLASS()
class AProgram060 : public AActor
{
    GENERATED_BODY()

public:
    AProgram060();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
