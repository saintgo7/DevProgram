// Camera Manager
// Program 085

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program085.generated.h"

UCLASS()
class AProgram085 : public AActor
{
    GENERATED_BODY()

public:
    AProgram085();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
