// USceneComponent
// Program 018

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program018.generated.h"

UCLASS()
class AProgram018 : public AActor
{
    GENERATED_BODY()

public:
    AProgram018();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
