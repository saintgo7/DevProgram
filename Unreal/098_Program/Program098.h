// World Subsystem
// Program 098

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program098.generated.h"

UCLASS()
class AProgram098 : public AActor
{
    GENERATED_BODY()

public:
    AProgram098();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
