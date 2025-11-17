// Axis Mapping
// Program 010

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program010.generated.h"

UCLASS()
class AProgram010 : public AActor
{
    GENERATED_BODY()

public:
    AProgram010();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
