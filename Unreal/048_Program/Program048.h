// User Widget
// Program 048

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program048.generated.h"

UCLASS()
class AProgram048 : public AActor
{
    GENERATED_BODY()

public:
    AProgram048();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
